from tkinter import * 

from configparser import ConfigParser  #proper configuration of files

from tkinter import messagebox 

import requests 

'''
{"coord":{"lon":75.1667,"lat":15.35},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],
"base":"stations","main":{"temp":299.17,"feels_like":299.17,"temp_min":299.17,"temp_max":299.17,"pressure":1010,"humidity":83},
"visibility":8000,"wind":{"speed":7.2,"deg":270},"clouds":{"all":75},"dt":1661151034,"sys":{"type":1,"id":9222,"country":"IN",
"sunrise":1661129146,"sunset":1661174356},"timezone":19800,"id":1269920,"name":"Hubli","cod":200}
'''

url_api= "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

 

#api_key = '8d50a70ad52c4813eb5009756b8673c9' 

api_file='wheather.key' 

file_a= ConfigParser() 

file_a.read(api_file) 

api_key = file_a['api_key']['key'] 



def weather_find(cord): 

    final = requests.get(url_api.format(cord,api_key)) 

    if final: 

        json_file = final.json() 

        city = json_file['name'] 

        country_name = json_file['sys']['country'] 

        k_temperature = json_file["main"]['temp']

        wind_speed = json_file["wind"]["speed"]

        wind_deg = json_file["wind"]["deg"]

        cord = json_file["coord"]

        c_temperature = k_temperature-273.15 

        f_temperature = (k_temperature-273.15)*9/5+32 

        weather_display = json_file['weather'][0]['main'] 

        result = (city,country_name,c_temperature,f_temperature,weather_display,wind_speed,wind_deg,cord) 

 

        return result 

    else: 

        return None 

 

def print_weather(): 

    city = search_city.get() 

    weather = weather_find(city) 

    if weather: 

        location_entry['text'] = '{}, {}'.format(weather[0], weather[1]) 

        temperature_entry['text'] = '{:.2f} C , {:.2f} F'.format(weather[2] , weather[3]) 

        weather_entry['text'] = weather[4] 

        speed_entry['text'] = weather[5]

        deg_entry['text'] = weather[6]

        cord_entry['text'] = weather[7]
 

    else: 

        messagebox.showerror('Error' , 'Please enter valid city') 

 

 

 

root = Tk() 

root.title("WEATHER FORECAST API") 

bg = PhotoImage(file = "R.png") 

label1 = Label(root, image = bg) 

label1.place(x = 120, y = 0) 

 

root.geometry("550x600") 

 

search_city = StringVar() 

enter_city = Entry(root , textvariable= search_city , justify=CENTER,  fg="black" , font=("Arial",30,"bold")) 

enter_city.pack() 

 

search_button = Button(root, text='SEARCH WEATHER', justify=CENTER, width=20 , background="white" , font=("Arial" , 25 , "bold"), command=print_weather) 

search_button.pack() 

 

location_entry = Label(root, text = 'Location:' , font = ("Arial" , 35 , "bold") , bg="lightblue") 
location_entry.pack(pady= 10) 

temperature_entry = Label(root, text='Temperature:', font = ("Arial" , 35 , "bold") , bg="lightblue") 
temperature_entry.pack(pady=10) 

speed_entry = Label(root,text="Speed (km/hr)",font = ("Arial" , 35 , "bold") , bg="lightblue")
speed_entry.pack(pady=10)

deg_entry = Label(root, text="Degrees",font = ("Arial" , 35 , "bold") , bg="lightblue" )
deg_entry.pack(pady=10)

cord_entry = Label(root, text="Coordinates",font = ("Arial" , 35 , "bold") , bg="lightblue" )
cord_entry.pack(pady=10)
 
weather_entry = Label(root, text= 'Condition' , font=("Arial" , 35 , "bold"), bg="lightblue") 
weather_entry.pack(pady= 10) 

root.mainloop() 

 