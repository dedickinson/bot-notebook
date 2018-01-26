#!/usr/bin/env python3

# Based on: https://github.com/simonmonk/raspberrypi_cookbook/blob/master/code/ardu_pi_i2c.py

import smbus

bus = smbus.SMBus(1)

DEVICE_ADDRESS = 0x04

while True:
    val = input("Switch on LED with 1, turn off with 0 (q to quit): ")
    if val in ['0', '1']:
        bus.write_byte(DEVICE_ADDRESS, int(val))
    elif val == 'q':
        break
    else:
        print("Sorry, I can't handle {}".format(val))
    
print("Bye")