#!/usr/bin/python
import smbus
import time

# Define some constants from the datasheet

DEVICE = 0x23 # Default device I2C address

# Start measurement at 0.5lx resolution. Time typically 120ms
CONTINUOUS_HIGH_RES_MODE_2 = 0x11

# Start measurement at 0.5lx resolution. Time typically 120ms
# Device is automatically set to Power Down after measurement.
#ONE_TIME_HIGH_RES_MODE_2 = 0x21

#bus = smbus.SMBus(0) # Rev 1
bus = smbus.SMBus(1)  # Rev 2 Pi uses 1

#function that to decimal number
#but why that division by 1.2
def convertToNumber(data):
  # Simple function to convert 2 bytes of data
  # into a decimal number
    return ((data[1] + (256 * data[0])) / 1.2)

#function that read level of light
def readLight(addr=DEVICE):
    data = bus.read_i2c_block_data(addr,CONTINUOUS_HIGH_RES_MODE_2)
    return convertToNumber(data)

#main function
def main():
    #print "Light Level : " + str(readLight()) + " lx"
    print "Light Level : " + str(readLight()) + " lx"

#run main function if was running this script
if __name__=="__main__":
   main()
