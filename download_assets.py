# -*- coding: utf-8 -*-
"""批量下载电工元件实物图到 assets 目录"""
import os
import urllib.request

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")

FILES = {
    "mcb.jpg": "https://aka.doubaocdn.com/s/yNxUeVmy4V",
    "rccb.jpg": "https://aka.doubaocdn.com/s/2dWWtCSuJX",
    "contactor.jpg": "https://aka.doubaocdn.com/s/gniB5Mlk8T",
    "thermal-relay.jpg": "https://aka.doubaocdn.com/s/ZvWFC8fElq",
    "relay.jpg": "https://aka.doubaocdn.com/s/sVry531UAk",
    "fuse.jpg": "https://aka.doubaocdn.com/s/jnVGzGElj8",
    "pushbutton.jpg": "https://aka.doubaocdn.com/s/FvpUY3Gg0U",
    "estop.jpg": "https://aka.doubaocdn.com/s/l7iaRNUUwv",
    "limit-switch.jpg": "https://aka.doubaocdn.com/s/JctUaUCQys",
    "indicator.jpg": "https://aka.doubaocdn.com/s/x7C5oN7bBZ",
    "proximity.jpg": "https://aka.doubaocdn.com/s/Gk9oGV5kQX",
    "photoelectric.jpg": "https://aka.doubaocdn.com/s/4UxzmdZJWN",
    "power-supply.jpg": "https://aka.doubaocdn.com/s/jByqSkf3Fp",
    "plc.jpg": "https://aka.doubaocdn.com/s/XBzDpV98Fl",
    "motor.jpg": "https://aka.doubaocdn.com/s/acPcQZAmBV",
    "multimeter.jpg": "https://aka.doubaocdn.com/s/HCEaiZHVZX",
    "terminal-block.jpg": "https://aka.doubaocdn.com/s/D54A9CB0MI",
    "solenoid.jpg": "https://aka.doubaocdn.com/s/xsbAuLy2Yd",
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
