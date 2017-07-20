from swiatlo import bh1750
from wil_temp import dht11

# print bh1750.readLight(35)

def check_hum_temp(pin):
    instance = dht11.DHT11(pin)
    result = instance.read()
    
    if result.is_valid():
        print("Temperature: %d C" % result.temperature)
        print("Humidity: %d %%" % result.humidity)
    else:
        print("Error: %d" % result.error_code)


check_hum_temp(15)
