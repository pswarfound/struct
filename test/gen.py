import json
import sys

def gen_content(js):
    headers = js['headers']
    w = ""
    for header in headers:
        w += "#include \"" + header + "\"\n"
    return w    

if __name__ == "__main__":
    js_path = sys.argv[1]
    dst_path = sys.argv[2]

    js = None
    with open(js_path, "r") as f:
        js = json.load(f)
        f.close()
    if js is None:
        exit()

    w = gen_content(js)
    with open(dst_path, "w") as f:
        f.write(w)
        f.close()