import pickle
import zomatopy
import json

config = {"user_key": "6ce88a5ec1419e335afa1c7f92f4b739"}
zomato = zomatopy.initialize_app(config)

cities = open('data/locations.txt').readlines()
city_list = [a.replace('\n','') for a in cities]
city_ids = []
for city in city_list:
	print(city.lower())
	r = zomato.get_location(city.lower())
	r = json.loads(r)
	print(r)
	city_id = r['location_suggestions'][0]['city_id']

	city_ids.append(city_id)
	

pickle.dump(city_ids,open('data/known_cities_id.pkl','wb'))
	
	