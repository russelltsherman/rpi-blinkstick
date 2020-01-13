#! /usr/bin/env python3

import blinkstick

bstick = blinkstick.find_by_serial("BS029570-3.0")

if bstick is None:
    print("Not found...")
else: 
    print("BlinkStick found. Current color: " + bstick.get_color(color_format="hex"))
