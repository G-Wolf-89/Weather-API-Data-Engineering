
import requests
import pandas as pd
import json

#request the page using the "request" package
url = "https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=-21.72&longitude=-45.39&start_date=2022-01-01&end_date=2023-12-31&hourly=temperature_2m,relative_humidity_2m,precipitation,surface_pressure"
page = requests.get(url)
converted = page.json()

# Pull your JSON data programmatically into your Python program, a
# and save this object into the path data/json.

with open("data/json/weather_api.json" , mode = "w") as file:
    #converts python object to json
    json.dump(converted, file, indent=4)  

#Remove all meta-data
hourly_data = converted['hourly']
json_data = { 
    "time" : hourly_data['time'],
    "temperature_2m": hourly_data["temperature_2m"],
    "relative_humidity_2m" : hourly_data["relative_humidity_2m"],
    "precipitation": hourly_data["precipitation"],
    "surface_pressure": hourly_data["surface_pressure"]
}
#your new dataframe w/o metadata
df = pd.DataFrame(json_data)

#Convert Json file with out metadata to CSV, 
df.to_csv('data/csv/weather_api.csv', index = False) 





