import json
import sys
import os
import subprocess

def gen_content(js):
    headers = js['headers']
    w = ""
    for header in headers:
        w += "#include \"" + header + "\"\n"
    return w    

if __name__ == "__main__":
    js_path = sys.argv[1]
    dst_dir = sys.argv[2]
    name = sys.argv[3]
    cflags = sys.argv[4]

    js = None
    with open(js_path, "r") as f:
        js = json.load(f)
        f.close()
    if js is None:
        exit()

    w = gen_content(js)
    dst_path = os.path.join(dst_dir, name + ".c")
    with open(dst_path, "w") as f:
        f.write(w)
        f.close()
    ef_dst_path = os.path.join(dst_dir, name + ".e")
    cmd = "gcc -E " + dst_path + " " + cflags + " > " + ef_dst_path
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    p = subprocess.Popen("rm -f " + dst_path, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()