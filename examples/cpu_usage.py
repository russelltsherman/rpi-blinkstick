#! /usr/bin/env python3

import blinkstick
import psutil

bstick = blinkstick.find_first()

if bstick is None:
    print("No BlinkSticks found...")
else:
    print("Displaying CPU usage (Green = 0%, Amber = 50%, Red = 100%)")
    print("Press Ctrl+C to exit")
    
    #go into a forever loop
    while True:
        cpu = psutil.cpu_percent(interval=1)
        intensity = int(255 * cpu / 100)

        bstick.set_color(red=intensity, green=255 - intensity, blue=0)