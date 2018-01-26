#!/usr/bin/env python3

import sys
import struct
from periphery import I2C, I2CError

DEVICE_ADDRESS = 0x15

try:
    i2c = I2C("/dev/i2c-1")
except (FileNotFoundError, I2CError) as e:
    print (e)
    sys.exit(1)

try:
    messages = [I2C.Message([1,2,3]), I2C.Message([0x00], read=True)]
    
    i2c.transfer(DEVICE_ADDRESS, messages)
    
    print(messages[1].data)

except (FileNotFoundError, I2CError) as e:
    print (e)
    sys.exit(1)
finally:
    i2c.close()


