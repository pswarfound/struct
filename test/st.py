#!/usr/bin/python
import os
import sys
import subprocess
import json

def locate_struct_def(lines, st_name):
    st = ""
    lb = 0
    rb = 0
    b = 0
    
    for ln in lines:
        ln.lstrip(" ")
        if ln == "" or ln[0] == "#" or ln[0] == "\n":
            continue
        if st == "" and ln.find(st_name) is not -1:
            v = st_name.split(" ")
            s = ln.split(" ")
            if v[0] != s[0]:
                continue
            if len(v) > 1 and v[1] != s[1]:
                continue
            st = st + ln
        elif st != "":
            st = st + ln
            
        if st != "":
            if ln.find("{") is not -1:
                lb = lb + 1
            if ln.find("}") is not -1:
                rb = rb + 1            
            b = lb - rb
            if b == 0:
                break
        
    return st

basic_type = [  "int8_t", "int16_t", "int32_t", "int64_t",
                "uint8_t", "uint16_t", "uint32_t", "uint64_t",
                "char", "short", "int", "long", "long long",
                "unsigned char", "unsigned short", "unsigned int", "unsigned long", "unsigned long long",
                "void", "size_t"]
const_basic_type = []

def gettp(st, mbr):
    s = st.rfind(mbr)
    ss = st.rfind(";", 0, s)
    if ss == -1:
        ss = st.find("{", 0, s) + 1
    tp = (st[ss:s].lstrip(";").strip("\n").lstrip(" "))

    return tp

def expand_start(st_name, out_list):
    st = locate_struct_def(codes, st_name)
    
    cmd = 'echo "offsets-of \\\"' + st_name + '\\\"\" | gdb a.out'
    print cmd
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    start = output.find("@@@@start")
    end = output.find("@@@@end")
    info = output[start + len("@@@@start"):end]
    print info
    print st
    info_list_tmp = info.split("\n")
    info_list = []
    for inf in info_list_tmp:
        inf = inf.lstrip(" ")
        if inf == "":
            continue
        info_list.append(inf)
#    print info_list
    for info in info_list:
        ele = info.split(" ")
        inf = {
            "type": "",
            "isp":-1,
            "isc":-1,
            "off": ele[0],
            "name": ele[1],
            "sub":[]
        }
        inf["type"] = gettp(st, ele[1])
        inf["isp"] = inf["type"].find("*") != -1
        inf["type"] = inf["type"].strip("*").rstrip(" ")
        sc = inf['type'].split(" ")
        
        if len(sc) > 2 :
            if sc[0] == "const":
                inf["type"] = inf["type"][6:]
                inf["isc"] = 1
        out_list.append(inf)
    print out_list
    for inf in out_list:
        print inf
        if inf['type'] not in basic_type and inf['type'] not in const_basic_type:
            if inf['type'] == "":
                continue
            print "expand"
            expand_start(inf['type'], inf['sub'])
        else:
            pass
        print inf
        
if __name__ == "__main__":
    for tp in basic_type:
        const_basic_type.append("const " + tp)

    fp = "./e"
#    st_name = "struct rte_mempool"
    st_name = "struct rte_mempool"
    codes = ""
    with open(fp, "r") as f:
        codes = f.readlines()
        f.close()
    root = []
    expand_start(st_name, root)
    print(json.dumps(root, indent=4))