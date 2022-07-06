import pandas as pd
import math
import numpy as np
import bs4
from bs4 import BeautifulSoup, NavigableString, Tag
import re
import requests
import lxml
import urllib.parse
from datetime import datetime  
from datetime import timedelta  

loc_weather = pd.read_csv("C:\\Users\John\\Downloads\\Historical PGA by loc.csv")

sample = loc_weather[['player','tournament name','pos','course', 'date']]
sample['weather'] = 0
sample['wind'] = 0

sample['city'] = sample['course'].str.split(',',expand = True)[0]
sample['city']= sample['city'].str.strip()
sample['state'] = sample['course'].str.split(',',expand = True)[1]
sample['state']= sample['state'].str.strip()

sample['date'] = pd.to_datetime(sample['date'], infer_datetime_format=True)
#sample['date'] = pd.to_datetime(sample['date']).date()
sample['date'] = sample['date'].dt.date

sample = sample.drop('course',axis=1)

tester = sample.drop(['player', 'pos'],axis = 1)
tester = tester.drop_duplicates()
tester.reset_index(inplace= True)


# day1

i = 0
x = 0
temp = []
wind = []

while x < len(tester['weather']):
    
    url = 'https://www.almanac.com/weather/history/{}/{}/{}'
    state = tester['state'][i] 
    city = tester['city'][i]
    date = tester['date'][i]

        
    w_url = url.format(state,city,date)
    
    try:
        # request the webpage
        res = requests.get(w_url)

        # return the text of the webpages
        soup = bs4.BeautifulSoup(res.text,"lxml")
        
       
        category = soup.findAll("table", attrs = {"class" : "weatherhistory_results"})
  
        
        # scraping the first table
        table1 = category[0]
 
        # acquire the temperature table data
        temp_report = table1.findAll("tr",attrs = {"class": "weatherhistory_results_datavalue temp"})
        wind_report = table1.findAll("tr",attrs = {"class": "weatherhistory_results_datavalue wdsp"})

        trep = temp_report[0] 
        wrep = wind_report[0]

          
        for item in trep.findAll("td"): # loop through all the elements
            # convert the the elements to text and strip "\n"
            item = (item.text).rstrip("\n")
            # append the clean column name to headings
            temp.append(item)
            
        for item in wrep.findAll("td"): # loop through all the elements
            # convert the the elements to text and strip "\n"
            item = (item.text).rstrip("\n")
            # append the clean column name to headings
            wind.append(item)
    
    except:
        temp.append(0)
        #wind.append(0)
        pass
           
    x = x + 1
    i = i + 1 
        
        
        
tester['weather'] = temp
tester['wind'] = wind

sample = sample.drop(['weather','wind'],axis = 1)
test_join = pd.merge(sample,tester, on = ['tournament name','date', 'city', 'state'],how = 'inner')

# extract non numeric characters from the float objects 

test_join['weather'] = test_join['weather'].str.extract('(\d+..)', expand=False)
test_join['wind'] = test_join['wind'].str.extract('(\d+..)', expand = False)

df = test_join
win = df[df['pos'] == 1]
win_temp = win.drop(['tournament name','date','city','state','wind','index'],axis = 1)#.groupby('player',as_index = True)
win_wind = win.drop(['tournament name','date','city','state','weather','index'],axis = 1)#.groupby('player',as_index = True)

five = df[df['pos'] < 6]
five_temp = five.drop(['tournament name','date','city','state','wind','index'],axis = 1)#.groupby('player',as_index = True)
five_wind = five.drop(['tournament name','date','city','state','weather','index'],axis = 1)#.groupby('player',as_index = True)

ten = df[df['pos'] < 10]
ten_temp = ten.drop(['tournament name','date','city','state','wind','index'],axis = 1)#.groupby('player',as_index = True)
ten_wind = ten.drop(['tournament name','date','city','state','weather','index'],axis = 1)#.groupby('player',as_index = True)

df['win_deg'] =  pd.merge(df,win_temp, on = ['player','pos'],how = 'inner')
test_join = pd.merge(sample,tester, on = ['tournament name','date', 'city', 'state'],how = 'inner')

# average wind/weather when player won

df['win_deg'] = win_temp['weather']

df['win_wind'] = win_wind['wind']

# average wind/weather for top 5

df['five_deg'] = five_temp['weather']

df['five_wind'] = five_wind['wind']

# average wind/weather for top 10

df['ten_deg'] = ten_temp['weather']

df['ten_wind'] = ten_wind['wind']




weather_data = df.drop('index',axis = 1)
weather_data = weather_data.fillna(0)
weather_data.to_csv("PGA weather by loc.csv")
