import requests
import geocoder      
class Weather:      
    def __init__(self):
       self.lat=None
       self.lon=None 
       self.api_id="92fc3554ba998907785a2ac38649a541"
<<<<<<< HEAD

=======
       user_input=input('''how would you like to proceed?
        1.Enter 1 to check live weather?
        2.Enter 2 to change your location?
>>>>>>> 0cd2fad800a9a403051e7fa200f3024f12bdaeaa
       self.get_current_location()

    def get_weather(self,lati,longi):
       self.lat=lati
       self.lon=longi
       base_url=f"https://api.openweathermap.org/data/2.5/weather?lat={self.lat}&lon={self.lon}&appid={self.api_id}"
       response=requests.get(base_url)
       data=response.json()
       print(data)
    
    def get_location_manually(self):
        address=input("enter the name of your city,state and country").replace(" ","+")
        url = f"https://nominatim.openstreetmap.org/search?q={address}&format=json"
        response = requests.get(url)
        data = response.json()
        if len(data) == 0:
           print("No results found")
        else:
            latitude = data[0]['lat']
            longitude = data[0]['lon']
            self.get_weather(latitude,longitude)

            
    def get_current_location(self):
        try:
            # Using geocoder to get the user's current location based on IP address
            current_location = geocoder.ip('me')
            latitude, longitude = current_location.latlng
            self.get_weather(latitude, longitude)
        except Exception as e:
            print(f"Error fetching current location automatically: {e}")
            print("Fetching location manually...")
            self.get_location_manually()

class Air_Quality(Weather):
   def __init__(self):
      super().__init__()
   

   def get_air_quality(self):
      url=f"http://api.openweathermap.org/data/2.5/air_pollution?lat={self.lat}&lon={self.lon}&appid={self.api_id}"
      response=requests.get(url)
      data=response.json()
      print(data)
d=Air_Quality()
d.get_air_quality()





      






    

