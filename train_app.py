# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=92fc3554ba998907785a2ac38649a541
import requests

class Weather:
    def __init__(self):
      
       user_input=input('''how would you like to proceed?
        1.Enter 1 to check live weather?
        2.Enter 2 to change your location?
        3.Enter 3 to exit''')
      
       if user_input=="1":
        print("live weather")
       elif user_input=="2":
        print("location change")
       elif user_input=="3":
        print("Exit")
    
    def get_location(self):
        address=input("enter the name of your city,state and country").replace(" ","+")
        url = f"https://nominatim.openstreetmap.org/search?q={address}&format=json"
        response = requests.get(url)
        data = response.json()
        if len(data) == 0:
           print("No results found")
        else:
            latitude = data[0]['lat']
            longitude = data[0]['lon']
        print(latitude,"     ",longitude)
d=Weather()
d.get_location()



    

