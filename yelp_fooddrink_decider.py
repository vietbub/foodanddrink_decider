import random
import apikey
from yelpapi import YelpAPI
import json

#Enter api_key
yelp_api=YelpAPI(apikey.api_key) #entered from separate API

address=input('Enter your address: ')

#calls yelp api for food and drink
food_res=yelp_api.search_query(term='Asian', location= address, radius=16000)#meters
drink_res=yelp_api.search_query(location=address, categories='bubbletea', radius=10000) #meters
food=[]
drink=[]

for x in food_res['businesses']:
    food.append(x['alias'])
for y in drink_res['businesses']:
    drink.append(y['alias'])

a = food[random.randint(0,len(food)-1)]
b = drink[random.randint(0,len(drink)-1)]

print(a)
print(b)
