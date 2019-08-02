#!/usr/bin/python
import os
import sys
import subprocess
import json
import copy
codes = ""

def getdup(s, c):
    cnt = 0
    for x in s:
        if x == c:
            cnt = cnt + 1
    return cnt

def parse_struct(st, mbr_list):
    lb = st.find("{")
    rb = st.rfind("}")
    if lb == -1 or rb == -1:
        return None
    inside = st[lb+1:rb]
    mbrs = inside.split(";")
    tmp_mbr = ""
    lb = 0
    rb = 0
    for idx, mbr in enumerate(mbrs):
        lb = lb + getdup(mbr, "{")
        rb = rb + getdup(mbr, "}")
        tmp_mbr = tmp_mbr + mbr + ";"
        if lb == rb:
            tmp_mbr = tmp_mbr.rstrip(";")
            tmp_mbr = tmp_mbr.strip("\n").strip(" ")
            if tmp_mbr != "":
                mbr_list.append(tmp_mbr)
                tmp_mbr = ""

def locate_struct_def(lines, st_name):
    st = ""
    lb = 0
    rb = 0
    b = 0
    cds = ""
    for ln in lines:
        ln = ln.replace("\n", " ")
        if ln == "":
            continue
        cds += ln
    start_pos = 0
    while True:
        key_start_pos = cds.find(st_name, start_pos)
        if key_start_pos is -1:
            break
        else:
            key_end_pos = key_start_pos + len(st_name)
            start_pos = key_end_pos
            if cds[key_start_pos - 1] not in [" ", "\n"] or \
                cds[key_end_pos] not in [" "]:
                continue
            skip = 0
            for c in cds[key_end_pos:]:
                if c == " ":
                    continue
                if c == "{":
                    break
                skip = 1
                break
            if skip == 1:
                continue
#            print cds[key_end_pos-len(st_name):key_end_pos+20]
            st = st_name
            for c in cds[key_end_pos:]:
                st += c
                if c == "{":
                    lb += 1
                elif c == "}":
                    rb += 1
                if lb == rb and c ==';':
                    break
            break
    return st

basic_type = [  "int8_t", "int16_t", "int32_t", "int64_t",
                "uint8_t", "uint16_t", "uint32_t", "uint64_t",
                "char", "short", "int", "long", "long long",
                "unsigned char", "unsigned short", "unsigned int", "unsigned long", "unsigned long long",
                "void", "size_t", "unsigned"]
l_types = ["long long", "unsigned long long", "int64_t", "uint64_t"]

def gettp(st, mbr):
    s = st.rfind(mbr)
    ss = st.rfind(";", 0, s)
    if ss == -1:
        ss = st.find("{", 0, s) + 1
    tp = (st[ss:s].lstrip(";").strip("\n").lstrip(" "))

    return tp

def parse_type_name(mbr_str):
    mbr_info = {
        "isc": False,
        "isp":False,
        "isa":False,
        "ac":0,
        "ise":False,
        "sub":[],
        "type":"",
        "name":"",
    }
    ars = mbr_str.find("[")
    are = mbr_str.find("]")
    if ars is not -1 and are is not -1:
        mbr_info["isa"] = True
        mbr_info["ac"] = mbr_str[ars+1:are]
        mbr_str = mbr_str[:ars]

    if mbr_str.find("*") is not -1:
        mbr_info["isp"] = True
    mbrs = mbr_str.split(" ")
    nmbr = len(mbrs)
    type_start = 0
    type_end = nmbr - 2
    #print mbrs
    if mbrs[0] == "const":
        mbr_info["isc"] = True
        type_start = 1
    if mbrs[type_start] == "enum":
        mbr_info["ise"] = True
        type_start += 1
        mbr_info["type"] = "int"
    if mbr_info["ise"] == False:
        for x in range(type_start, type_end + 1):
            mbr_info["type"] = mbr_info["type"] + " " + mbrs[x]
            mbr_info["type"] = mbr_info["type"].strip(" ") 
    mbr_info["name"] = mbrs[nmbr - 1].strip("*")
    #print mbr_info
    return mbr_info

def expand_start(st_name, out_list):
#    print "@@@@@@@@@@@" + st_name
    st_real = st_name.split(" ")
    st = locate_struct_def(codes, st_real[len(st_real) - 1])
  #  print st
    mbr_list = []
    parse_struct(st, mbr_list)
   # print mbr_list
    for mbr in mbr_list:
        if getdup(mbr, "{") != 0:
            continue
        mbr_info = parse_type_name(mbr)
        if mbr_info["type"] not in basic_type and mbr_info["isp"] == False:
            expand_start(mbr_info["type"], mbr_info['sub'])
        out_list.append(mbr_info)

def write_mbr(name, mbr_list, f, lv, parent):
    if lv != 1:
        w = "    ret = snprintf(p, left, "
        w += "\"" + " "*4*(lv - 1) + name + ": \\n\");"
        w += " CHECK(ret, p, left);\n"
        f.write(w) 
    for mbr in mbr_list:
        if len(mbr['sub']) == 0:
            w = "    ret = snprintf(p, left, "
            w += "\"" + " "*4*lv + mbr['name'] + ": "
            if mbr['isp'] == True:
                w += "p=%p"
            elif mbr['isa'] == True:
                pass
            elif mbr['type'] in l_types:
                w += "0x%lx"
            elif mbr['type'] == "size_t":
                w += "%z"
            elif mbr['type'] in basic_type:
                w += "0x%x"
            else:
                pass
            w += "\\n\""
            w += ", " + parent
            w += mbr["name"]
            w += ");"
            #w += "\n"
            w += " CHECK(ret, p, left);\n"
            f.write(w)
        else:
            np = parent + mbr['name']+"."
            write_mbr(mbr['name'], mbr['sub'], f, lv + 1, np)
CHECK_STR = "#define CHECK(ret, p, left) \\\n\
    if (ret >= left) { \\\n\
        return;\\\n\
    }\\\n\
    p += ret;left -= ret;\n"

def gen_c_file(root, js, cfile_path):
    f = open(cfile_path, "w")
    headers = js['headers']
    w = ""
    for header in headers:
        w += "#include \"" + header + "\"\n"
    w += "\n"
    f.write(w)
    f.write(CHECK_STR)
    f.write("\n")
    for st_root in root:
        type = st_root["type"]
        w = "void struct_" + type.replace(" ", "_") +"_print(" + type + " *t, char *buf, int sz)\n"
        w += "{\n"
        w += "    int ret;\n    char *p=buf;\n    int left = sz;\n"
        f.write(w)
        mbrs = st_root['mbrs']
        write_mbr(type, mbrs, f, 1, "t->")
        w = "}\n\n"
        f.write(w)
    f.close()

if __name__ == "__main__":
    js_path = sys.argv[1]
    tmp_dir = sys.argv[2]
    dst_dir = sys.argv[3]
    name = sys.argv[4]
    sc_file = os.path.join(tmp_dir, name + ".e")
    cfile_path = os.path.join(dst_dir, name + ".c")
    js = None

    with open(js_path, "r") as f:
        js = json.load(f)
        f.close()

    f = None
    try:
        f = open(sc_file, "r")
    except Exception as e:
        print e
        exit()
    try:
        codes = f.readlines()
    except Exception as e:
        print e
        exit()
    try:        
        f.close()
    except Exception as e:
        print e
        exit()
    tmp = copy.deepcopy(codes)

    for idx, code in enumerate(tmp):
        if code[0] == "#":
            codes.remove(code)

    st_names = js['structs']
    root = []
    for st_name in st_names:
        st_root = {
            "type":st_name,
            "mbrs":[]
        }
        name_list = st_name.split(" ")
        real_name = name_list[len(name_list) - 1]
        expand_start(real_name, st_root["mbrs"])
#        print(json.dumps(root, indent=4))
        root.append(st_root)
    gen_c_file(root, js, cfile_path)