import sys
import json
from client import DCT2Engine

def main():
    dct = DCT2Engine()
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        req = json.loads(line)
        method = req.get("method")
        params = req.get("params", {})
        if method == "dct":
            c = dct.dct2(params.get("signal", []))
            res = {"coefficients": c}
        elif method == "idct":
            s = dct.idct2(params.get("coefficients", []))
            res = {"signal": s}
        else:
            res = {"error": "unknown method"}
        sys.stdout.write(json.dumps({"id": req.get("id"), "result": res}) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
