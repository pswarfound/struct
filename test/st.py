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
                ]
const_basic_type = []

def gettp(st, mbr):
    s = st.rfind(mbr)
    ss = st.rfind(";", 0, s)
    if ss == -1:
        ss = st.find("{", 0, s) + 1
    tp = (st[ss:s].lstrip(";").strip("\n").lstrip(" "))

    return tp

if __name__ == "__main__":
    for tp in basic_type:
        const_basic_type.append("const " + tp)

    fp = "./e"
#    st_name = "struct rte_mempool"
    st_name = "struct rte_eth_dev_info"
    codes = ""
    with open(fp, "r") as f:
        codes = f.readlines()
        f.close()
    
    st = locate_struct_def(codes, st_name)
    #print st
    cmd = 'echo "offsets-of \\\"' + st_name + '\\\"\" | gdb a.out'
    
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    #print "Command output : ", output
    start = output.find("@@@@start")
    end = output.find("@@@@end")
    info = output[start + len("@@@@start"):end]
    
    info_list_tmp = info.split("\n")
    info_list = []
    for inf in info_list_tmp:
        inf = inf.lstrip(" ")
        if inf == "":
            continue
        info_list.append(inf)
    
    inf_list = []
    
    for info in info_list:
        ele = info.split(" ")
        inf = {
            "type": "",
            "isp":-1,
            "off": ele[0],
            "name": ele[1],
            "sub":[]
        }
        inf["type"] = gettp(st, ele[1])
        inf["isp"] = inf["type"].find("*") != -1
        inf["type"] = inf["type"].strip("*").rstrip(" ")
        inf_list.append(inf)

#    print inf_list
    print "check sub"
    for inf in inf_list:
        if inf['type'] not in basic_type and inf['type'] not in const_basic_type:
            sst = locate_struct_def(codes, inf['type'])

            print sst
            cmd = 'echo "offsets-of \\\"' + inf['type'] + '\\\"\" | gdb a.out'
            
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
            (output, err) = p.communicate()
            p_status = p.wait()
            #print "Command output : ", output
            start = output.find("@@@@start")
            end = output.find("@@@@end")
            info = output[start + len("@@@@start"):end]
            print info
            s_list_tmp = info.split("\n")
            info_list = []
            for info in s_list_tmp:
                info = info.lstrip(" ")
                if info == "":
                    continue
                info_list.append(info)
            
            s_list = inf["sub"]
            
            for info in info_list:
                ele = info.split(" ")
                ii = {
                    "type": "",
                    "isp":-1,
                    "off": ele[0],
                    "name": ele[1],
                    "sub":[]
                }
                ii["type"] = gettp(sst, ele[1])
                ii["isp"] = ii["type"].find("*") != -1
                ii["type"] = ii["type"].strip("*").rstrip(" ")
                s_list.append(ii)
        else:
            pass
    print(json.dumps(inf_list, indent=4))