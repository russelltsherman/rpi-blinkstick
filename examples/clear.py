#! /usr/bin/env python3

import blinkstick

for bstick in blinkstick.find_all():
    bstick.turn_off()
    print(bstick.get_serial() + " turned off")