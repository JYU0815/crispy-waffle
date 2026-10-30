# -*- coding: utf-8 -*-
"""批量下载进阶元件实物图到 assets 目录"""
import os
import urllib.request

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")

FILES = {
    "vfd.jpg": "https://aka.doubaocdn.com/s/OammX35TXQ",
    "servo.jpg": "https://aka.doubaocdn.com/s/EKyoKGIKwI",
    "stepper.jpg": "https://aka.doubaocdn.com/s/jgoZnrvVtJ",
    "hmi.jpg": "https://aka.doubaocdn.com/s/BkJXA2wddG",
    "encoder.jpg": "https://aka.doubaocdn.com/s/TM3iHhOp5E",
    "safety-relay.jpg": "https://aka.doubaocdn.com/s/yzew8Q7CIU",
}

req_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

ok, fail = 0, 0
for name, url in FILES.items():
    dest = os.path.join(BASE, name)
    try:
        req = urllib.request.Request(url, headers=req_headers)
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = resp.read()
        if len(data) < 5000:
            print("FAIL %s: too small %d bytes" % (name, len(data)))
            fail += 1
            continue
        with open(dest, "wb") as f:
            f.write(data)
        print("OK   %s  %d KB" % (name, len(data) // 1024))
        ok += 1
    except Exception as e:
        print("FAIL %s: %s" % (name, e))
        fail += 1

print("---- done: %d ok, %d fail ----" % (ok, fail))
