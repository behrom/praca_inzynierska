from pymongo import MongoClient

client = MongoClient('localhost', 27017)

pots = client.pots

def save_config(coll, light_pin = -1, hum_temp_pin = -1, soil_moisture_pin = -1):
    config = {}

    if(light_pin != -1):
        config['light_pin'] = light_pin

    if(hum_temp_pin != -1):
        config["hum_temp_pin"] = hum_temp_pin

    if(soil_moisture_pin != -1):
        config["soil_moisture_pin"] = soil_moisture_pin

    print coll.update_one({'_id':'config'}, {"$set": config}, True)

#run function if was running this script
if __name__ == "__main__":
    save_config(pots.pot1, 35, 15)
