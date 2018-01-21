#!/usr/bin/env python3

import struct
import smbus

bus = smbus.SMBus(1)

DEVICE_ADDRESS = 0x04

def get_float(data, index):
    bytes = data[4*index:(index+1)*4]
    return struct.unpack('f', "".join(map(chr, bytes)))[0]

data = bus.read_i2c_block_data(DEVICE_ADDRESS, 0)
print(data)
print(get_float(data, 0))
print(get_float(data, 1))

