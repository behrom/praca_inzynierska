from pymongo import MongoClient

client = MongoClient('localhost', 27017)

pots = client.pots

for col in pots.collection_names(include_system_collections=False):
    for document in pots.get_collection(col).find({"_id": "config"}):
        print col, document

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
