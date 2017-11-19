#!/usr/bin/python
import spidev
import time
import math

"""YL-69-ShowkHumidityValue.py : Show current humidity sensor value """
__author__ = "zbiros"
__copyright__ = "Copyright 2015, Malinowo.net.pl"
__credits__ = ["maros"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "zbiros"
__email__ = "zbiros@malinowo.secu.com.pl"
__status__ = "Development"

spi = spidev.SpiDev()
spi.open(0, 0)

def readadc(adcnum):
    if adcnum > 7 or adcnum < 0:
        return -1
    r = spi.xfer2([1, (8 + adcnum) << 4, 0])
    adcout = ((r[1] & 3) << 8) + r[2]
    return adcout

def percentage(part, whole):
  return 100 * int(part)/int(whole)

while True:

    value = readadc(0)
    volts = float("{0:.2f}".format((value * 3.3) / 1024))

    if value < 255:
       print "poziom wilgotnosci powyzej 75 %"
    if value > 255 and value < 512:
       print "poziom wilgotnosci w normie"
    if value > 512:
       print "zbyt sucha gleba,podlej kwiatek"

    percent = 100 - int(math.floor(percentage(value,1023)))
    print `value` + "|" + `volts` + "V|" + `percent` + "%"
    time.sleep(5)
