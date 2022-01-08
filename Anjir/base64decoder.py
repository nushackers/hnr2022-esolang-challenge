#!/usr/bin/env python3

import base64

with open("main.piet.b64") as f:
    b64str = f.read()
    outstr = base64.b64decode(b64str)
    with open("main.piet", "wb") as out:
        out.write(outstr)
