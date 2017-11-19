# -*- coding: utf-8 -*-
from pymongo import MongoClient
from swiatlo import bh1750
from wil_temp import dht11
import datetime

def check_hum_temp(pin):
    instance = dht11.DHT11(pin)
    result = instance.read()

    # powinienem to jakoś obsluzyc
    #if result.is_valid():
        #print("Temperature: %d C" % result.temperature)
        #print("Humidity: %d %%" % result.humidity)
    #else:
        #print("Error: %d" % result.error_code)

    if result.is_valid():
        return (result.temperature, result.humidity)

def check_light_level(pin):
    # chyba powinienem zabezpieczyc te wyniki poprzez 3 krotne sprawdzeniez
    # wartosci bo czasem jak nie ma wyniku zwraca 0.0 nawet w sloneczny dzien
    return bh1750.readLight(pin)


def save_measurement_in_database():
    client = MongoClient('localhost', 27017)
    pots = client.pots

    for col in pots.collection_names(include_system_collections=False):
        for document in pots.get_collection(col).find({"_id": "config"}):
            measurement = {}
            
	    humidity_temp = None
	    while humidity_temp is None:
	        humidity_temp = check_hum_temp(document['hum_temp_pin'])
            
            measurement['temperature'] = humidity_temp[0]
            measurement['humidity'] = humidity_temp[1]
            measurement['illuminance'] = check_light_level(document['light_pin'])
            measurement['date'] = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            #print pots.get_collection(col).insert_one(measurement)
	    print measurement

def get_all_from_database():
    client = MongoClient('localhost', 27017)
    pots = client.pots

    for col in pots.collection_names(include_system_collections=False):
        for document in pots.get_collection(col).find():
            print col, document

#run function if was running this script
if __name__ == "__main__":
    save_measurement_in_database()
