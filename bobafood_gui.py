from tkinter import *
import sys
import random

#Use yelp
from yelpapi import YelpAPI
client_id= "EvNOXT0xyq4fjhkMp7BffA"
client_secret= "EbKN2SfGLxX1WxVEWWd73mfuyRhzRWgNFGIvsOoxAJkWh8StnfdmCJL5FOyHu0Tt"
yelp_api = YelpAPI(client_id, client_secret)


#GUI
window=Tk()
window.title("Food and Boba decider")
window.geometry("500x700") #sets geometry
#text_entry
txt= Entry(window,width=40)
txt.grid(column=2,row=0,padx=20)
lbl= Label(window,text="Please enter address")
lbl.grid(column=1, row=0)
#textbox
text_box=Text(window,height=4,width=40)#,state=DISABLED)
text_box.grid(column=2,row=3)

def set():
    address=txt.get()
    food_results = yelp_api.search_query(term='asian restaurant', location= address,radius = 4828)#4828 meter radius
    drink_results= yelp_api.search_query(term='boba',location=address, radius=4828,categories= 'bubbletea')
    #creates list to be used for app
    drinkPlaces = []
    foodPlaces = []

def food():
    address=txt.get()
    address = txt.get()
    food_results = yelp_api.search_query(term='asian restaurant', location=address, radius=4828)  # 4828 meter radius
    drink_results = yelp_api.search_query(term='boba', location=address, radius=4828, categories='bubbletea')
    # creates list to be used for app
    foodPlaces = []
    for x in food_results['businesses']:
        foodPlaces.append(x['name'])

    a = foodPlaces[random.randint(0,len(foodPlaces)-1)]
    text_box.delete(1.0,END)
    text_box.insert(END, "The choice is " + a)
def drink():
    address = txt.get()
    address = txt.get()
    food_results = yelp_api.search_query(term='asian restaurant', location=address, radius=4828)  # 4828 meter radius
    drink_results = yelp_api.search_query(term='boba', location=address, radius=4828, categories='bubbletea')
    # creates list to be used for app
    drinkPlaces = []
    for x in drink_results['businesses']:
        drinkPlaces.append(x['name'])

    b = drinkPlaces[random.randint(0, len(drinkPlaces) - 1)]
    text_box.delete(1.0,END)
    text_box.insert(END,"The choice is "+b)

def both():
    address = txt.get()
    address = txt.get()
    food_results = yelp_api.search_query(term='asian restaurant', location=address, radius=4828)  # 4828 meter radius
    drink_results = yelp_api.search_query(term='boba', location=address, radius=4828, categories='bubbletea')
    # creates list to be used for app
    drinkPlaces = []
    foodPlaces = []
    for x in food_results['businesses']:
        foodPlaces.append(x['name'])
    for y in drink_results['businesses']:
        drinkPlaces.append(y['name'])
    a = foodPlaces[random.randint(0, len(foodPlaces) - 1)]
    b = drinkPlaces[random.randint(0,len(drinkPlaces)-1)]
    text_box.delete(1.0,END)
    text_box.insert(END, "The choices are " + a + " and "+ b)

def buttos():
    btnf= Button(window, text="food",command=food)
    btnd= Button(window,text='drink',command=drink)
    btnb= Button (window, text= 'both',command=both)

    btnf.grid(column=1, row=1)
    btnd.grid(column=2,row=1)
    btnb.grid(column=3,row=1)

btn0= Button(window,text='submit', command=buttos)
btn0.grid(column=3, row =0)





window.mainloop()