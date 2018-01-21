#!/usr/bin/env python3
# This script is paired with i2c_basic.ino
# sudo apt install python3-smbus

# Command line tips
# Check your i2c connection with:
#    i2cdetect -y 1
# Request a value from the Arduino:
#    i2cget -y 1
# Send a number (16) to the Arduino
#    i2cset -y 1 16

# Crappy doco at http://wiki.erazor-zone.de/wiki:linux:python:smbus:doc

from random import randint
import smbus

DEVICE_ADDRESS = 0x04
DEVICE_REG_MODE1 = 0x00

bus = smbus.SMBus(1)

# Read
output = int(bus.read_byte(DEVICE_ADDRESS))
print("Received {}".format(output))

# Write
input = randint(0,99)
bus.write_byte(DEVICE_ADDRESS, input)
print("Sent {}".format(input))

bus.close()

    


