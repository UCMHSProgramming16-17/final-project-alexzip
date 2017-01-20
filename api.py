#open file
#file = open('list.txt', 'w')

import requests

endpoint = 'https://api.darksky.net/forecast/'
key = '1db82b08bc0a612ca4d6e1039c1c7707'

latList = []
tempList = []

for x in range(0,100,10):
    lat = str(x)
    lon = '74.35608'
    url = endpoint + key + '/' + lat + ',' + lon
    
    r = requests.get(url)

    weather = r.json()
    #keys; currently, daily, latitude, longitude, offset
    #flags, minutely, hourly, timezone
    Max = weather['daily']['data'][0]['temperatureMax']
    
    latList.append(float(lat))
    tempList.append(Max)

import pandas as pd

df = pd.DataFrame({
    'lat' : latList, 
    'temp' : tempList
})

print(df)

from bokeh.charts import Bar, output_file, save

chart = Bar(df, 'lat', values='temp', title='Temperature by latitude')

output_file('tempVlat.html')
 
save(chart)




