#! /usr/bin/env python3

import blinkstick

for bstick in blinkstick.find_all():
    bstick.set_random_color()
    print(bstick.get_serial() + " " + bstick.get_color(color_format="hex"))