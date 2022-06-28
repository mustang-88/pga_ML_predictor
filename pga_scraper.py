# run years as functions until a better solution is obtained
# match excel sheet features in output
# create function that returns combos
# print combos as a webbapp with chart of most likely to win

import pandas as pd
import numpy as np
import bs4
from bs4 import BeautifulSoup # NavigableString, Tag
import re
import requests
# import json
from selenium import webdriver
import time
from datetime import date
# from decimal import Decimal



def acc22():
    url = 'https://www.pgatour.com/stats/stat.102.y2022.html'
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text,"lxml")
    category = soup.findAll("table", attrs = {"class" : "table-styled"})

    # scraping the first table
    table1 = category[0]
    # the head will form our column names
    stats = table1.findAll("th",attrs = {"class": ["rank-this","rank-last","player-name","rounds","col-stat"]})

    # Head values (COlumn names) are the first items of the body list
    #header = body[0] #0th item is the header row

    # return the header names of the columns in the first row
    headers = []
    # check the number of headers
    for x in range(len(stats)):
        # check the value count and return their names
        for var in stats[x]:
            headers.append(var)

    headers.pop(0)
    headers[0] = headers[0].text


    body = []

    # find all the rows containing the "tr" element
    # body_rows = soup.find_all("td", attrs = {"class" : ["player-name","hidden-small"]})
    body_rows = soup.find_all("tr")

    # check each page for the element and add the rows into body
    for rows in body_rows:
        body.append(rows)


    player = [] # will be a list for list for all rows

    for row_num in range(len(body)): # a row at a time
        row = [] # this will add old entries for one row
        # use find all in the code below to scrape specifically through the needed tags and avoid a navig/no text error
        for row_item in body[row_num].find_all("td"): # loop through all row entries
                # row_item.text removes the tags from the entries
                # the following regex is to remove \xao and \n and commas from row_item.text
                # the xa0 encodes the flag, \n is the newline and comma separates thousands in numbers
            aa = re.sub("(\xa0)|(\n)|,","",row_item.text)
                # append aa to row - note one row entry is being appended
            row.append(aa)
            # append one row to all_rows
        player.append(row)

            # dump the first row of non-player information as well as any rows that may match using list comprehension
        # the code is run twice temporarily until a better script is obtained

    player = [x for x in player if x != player[0]]
    player = [x for x in player if x != player[0]]

        # create a dataframe using the player as data and headings as the column names
    acc22 = pd.DataFrame(data = player,columns=headers)
    acc22 = acc22.drop(columns = ['THIS WEEK','\n                                RANK LAST WEEK'])
        # delete the unecessary columns

    acc22['Avg Fairs Hit'] = pd.to_numeric(acc22['FAIRWAYS HIT']) / pd.to_numeric(acc22['POSSIBLE FAIRWAYS'])

    return acc22

acc22 = acc22()


def dr22():
    url = 'https://www.pgatour.com/content/pgatour/stats/stat.101.y2022.html'
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text,"lxml")
    category = soup.findAll("table", attrs = {"class" : "table-styled"})

    # scraping the first table
    table1 = category[0]
    # the head will form our column names
    stats = table1.findAll("th",attrs = {"class": ["rank-this","rank-last","player-name","rounds","col-stat"]})

    # Head values (COlumn names) are the first items of the body list
    #header = body[0] #0th item is the header row

    # return the header names of the columns in the first row
    headers = []
    # check the number of headers
    for x in range(len(stats)):
        # check the value count and return their names
        for var in stats[x]:
            headers.append(var)

    headers.pop(0)
    headers[0] = headers[0].text

    body = []

        # find all the rows containing the "tr" element
    # body_rows = soup.find_all("td", attrs = {"class" : ["player-name","hidden-small"]})
    body_rows = soup.find_all("tr")

    # check each page for the element and add the rows into body
    for rows in body_rows:
        body.append(rows)

    player = [] # will be a list for list for all rows

    for row_num in range(len(body)): # a row at a time
        row = [] # this will add old entries for one row
        # use find all in the code below to scrape specifically through the needed tags and avoid a navig/no text error
        for row_item in body[row_num].find_all("td"): # loop through all row entries
                # row_item.text removes the tags from the entries
                # the following regex is to remove \xao and \n and commas from row_item.text
                # the xa0 encodes the flag, \n is the newline and comma separates thousands in numbers
            aa = re.sub("(\xa0)|(\n)|,","",row_item.text)
                # append aa to row - note one row entry is being appended
            row.append(aa)
            # append one row to all_rows
        player.append(row)

            # dump the first row of non-player information as well as any rows that may match using list comprehension
        # the code is run twice temporarily until a better script is obtained

    player = [x for x in player if x != player[0]]
    player = [x for x in player if x != player[0]]



    # create a dataframe using the player as data and headings as the column names
    dr22 = pd.DataFrame(data = player,columns=headers)
    dr22 = dr22.drop(columns = ['THIS WEEK','\n                                RANK LAST WEEK'])
    # delete the unecessary columns


    # create a dataframe using the player as data and headings as the column names
    dr22 = pd.DataFrame(data = player,columns=headers)
    dr22 = dr22.drop(columns = ['THIS WEEK','\n                                RANK LAST WEEK'])
    # delete the unecessary columns

    dr22['Drives AVG'] = pd.to_numeric(dr22['AVG.']) *1 /100
    dr22.head()

    return dr22

dr22 = dr22()


def gr22():
    url = 'https://www.pgatour.com/stats/stat.103.y2022.html'
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text,"lxml")
    category = soup.findAll("table", attrs = {"class" : "table-styled"})

    # scraping the first table
    table1 = category[0]
    # the head will form our column names
    stats = table1.findAll("th",attrs = {"class": ["rank-this","rank-last","player-name","rounds","col-stat"]})

    # Head values (COlumn names) are the first items of the body list
    #header = body[0] #0th item is the header row

    # return the header names of the columns in the first row
    headers = []
    # check the number of headers
    for x in range(len(stats)):
        # check the value count and return their names
        for var in stats[x]:
            headers.append(var)

    headers.pop(0)
    headers[0] = headers[0].text

    body = []

    # find all the rows containing the "tr" element
    # body_rows = soup.find_all("td", attrs = {"class" : ["player-name","hidden-small"]})
    body_rows = soup.find_all("tr")

    # check each page for the element and add the rows into body
    for rows in body_rows:
        body.append(rows)

    player = [] # will be a list for list for all rows

    for row_num in range(len(body)): # a row at a time
        row = [] # this will add old entries for one row
        # use find all in the code below to scrape specifically through the needed tags and avoid a navig/no text error
        for row_item in body[row_num].find_all("td"): # loop through all row entries
                # row_item.text removes the tags from the entries
                # the following regex is to remove \xao and \n and commas from row_item.text
                # the xa0 encodes the flag, \n is the newline and comma separates thousands in numbers
            aa = re.sub("(\xa0)|(\n)|,","",row_item.text)
                # append aa to row - note one row entry is being appended
            row.append(aa)
            # append one row to all_rows
        player.append(row)


            # dump the first row of non-player information as well as any rows that may match using list comprehension
        # the code is run twice temporarily until a better script is obtained

    player = [x for x in player if x != player[0]]
    player = [x for x in player if x != player[0]]

        # create a dataframe using the player as data and headings as the column names
    gr22 = pd.DataFrame(data = player,columns=headers)
    gr22 = gr22.drop(columns = ['THIS WEEK','\n                                RANK LAST WEEK'])
        # delete the unecessary columns

    gr22['Gr in Reg'] = pd.to_numeric(gr22['RELATIVE/PAR'])

    return gr22

gr22 = gr22()


def prx22():
    url = 'https://www.pgatour.com/stats/stat.331.y2022.html'
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text,"lxml")
    category = soup.findAll("table", attrs = {"class" : "table-styled"})

    # scraping the first table
    table1 = category[0]
    # the head will form our column names
    stats = table1.findAll("th",attrs = {"class": ["rank-this","rank-last","player-name","rounds","col-stat"]})

    # Head values (COlumn names) are the first items of the body list
    #header = body[0] #0th item is the header row

    # return the header names of the columns in the first row
    headers = []
    # check the number of headers
    for x in range(len(stats)):
        # check the value count and return their names
        for var in stats[x]:
            headers.append(var)

    headers.pop(0)
    headers[0] = headers[0].text

    body = []

    # find all the rows containing the "tr" element
    # body_rows = soup.find_all("td", attrs = {"class" : ["player-name","hidden-small"]})
    body_rows = soup.find_all("tr")

    # check each page for the element and add the rows into body
    for rows in body_rows:
        body.append(rows)

    player = [] # will be a list for list for all rows

    for row_num in range(len(body)): # a row at a time
        row = [] # this will add old entries for one row
        # use find all in the code below to scrape specifically through the needed tags and avoid a navig/no text error
        for row_item in body[row_num].find_all("td"): # loop through all row entries
                # row_item.text removes the tags from the entries
                # the following regex is to remove \xao and \n and commas from row_item.text
                # the xa0 encodes the flag, \n is the newline and comma separates thousands in numbers
            aa = re.sub("(\xa0)|(\n)|,","",row_item.text)
                # append aa to row - note one row entry is being appended
            row.append(aa)
            # append one row to all_rows
        player.append(row)

            # dump the first row of non-player information as well as any rows that may match using list comprehension
        # the code is run twice temporarily until a better script is obtained

    player = [x for x in player if x != player[0]]
    player = [x for x in player if x != player[0]]

        # create a dataframe using the player as data and headings as the column names
    prx22 = pd.DataFrame(data = player,columns=headers)
    prx22 = prx22.drop(columns = ['THIS WEEK','\n                                RANK LAST WEEK'])
        # delete the unecessary columns


    prx22['Proximity Carry'] = pd.to_numeric(prx22['# OF ATTEMPTS']) / pd.to_numeric(prx22['TOTAL DISTANCE (FEET)'])

    return prx22

prx22 = prx22()

def par3_22():
    url = 'https://www.pgatour.com/content/pgatour/stats/stat.171.y2022.html'
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text,"lxml")
    category = soup.findAll("table", attrs = {"class" : "table-styled"})

    # scraping the first table
    table1 = category[0]
    # the head will form our column names
    stats = table1.findAll("th",attrs = {"class": ["rank-this","rank-last","player-name","rounds","col-stat"]})

    # Head values (COlumn names) are the first items of the body list
    #header = body[0] #0th item is the header row

    # return the header names of the columns in the first row
    headers = []
    # check the number of headers
    for x in range(len(stats)):
        # check the value count and return their names
        for var in stats[x]:
            headers.append(var)

    headers.pop(0)
    headers[0] = headers[0].text

    body = []

    # find all the rows containing the "tr" element
    # body_rows = soup.find_all("td", attrs = {"class" : ["player-name","hidden-small"]})
    body_rows = soup.find_all("tr")

    # check each page for the element and add the rows into body
    for rows in body_rows:
        body.append(rows)

    player = [] # will be a list for list for all rows

    for row_num in range(len(body)): # a row at a time
        row = [] # this will add old entries for one row
        # use find all in the code below to scrape specifically through the needed tags and avoid a navig/no text error
        for row_item in body[row_num].find_all("td"): # loop through all row entries
                # row_item.text removes the tags from the entries
                # the following regex is to remove \xao and \n and commas from row_item.text
                # the xa0 encodes the flag, \n is the newline and comma separates thousands in numbers
            aa = re.sub("(\xa0)|(\n)|,","",row_item.text)
                # append aa to row - note one row entry is being appended
            row.append(aa)
            # append one row to all_rows
        player.append(row)

            # dump the first row of non-player information as well as any rows that may match using list comprehension
        # the code is run twice temporarily until a better script is obtained

    player = [x for x in player if x != player[0]]
    player = [x for x in player if x != player[0]]

        # create a dataframe using the player as data and headings as the column names
    par3_22 = pd.DataFrame(data = player,columns=headers)
    par3_22 = par3_22.drop(columns = ['THIS WEEK','\n                                RANK LAST WEEK'])
        # delete the unecessary columns


    par3_22['Par3'] = pd.to_numeric(par3_22['PAR 3 AVG'])

    return par3_22

par3_22 = par3_22()


def par4_22():
    url = 'https://www.pgatour.com/content/pgatour/stats/stat.172.y2022.html'
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text,"lxml")
    category = soup.findAll("table", attrs = {"class" : "table-styled"})

    # scraping the first table
    table1 = category[0]
    # the head will form our column names
    stats = table1.findAll("th",attrs = {"class": ["rank-this","rank-last","player-name","rounds","col-stat"]})

    # Head values (COlumn names) are the first items of the body list
    #header = body[0] #0th item is the header row

    # return the header names of the columns in the first row
    headers = []
    # check the number of headers
    for x in range(len(stats)):
        # check the value count and return their names
        for var in stats[x]:
            headers.append(var)

    headers.pop(0)
    headers[0] = headers[0].text

    body = []

    # find all the rows containing the "tr" element
    # body_rows = soup.find_all("td", attrs = {"class" : ["player-name","hidden-small"]})
    body_rows = soup.find_all("tr")

    # check each page for the element and add the rows into body
    for rows in body_rows:
        body.append(rows)

    player = [] # will be a list for list for all rows

    for row_num in range(len(body)): # a row at a time
        row = [] # this will add old entries for one row
        # use find all in the code below to scrape specifically through the needed tags and avoid a navig/no text error
        for row_item in body[row_num].find_all("td"): # loop through all row entries
                # row_item.text removes the tags from the entries
                # the following regex is to remove \xao and \n and commas from row_item.text
                # the xa0 encodes the flag, \n is the newline and comma separates thousands in numbers
            aa = re.sub("(\xa0)|(\n)|,","",row_item.text)
                # append aa to row - note one row entry is being appended
            row.append(aa)
            # append one row to all_rows
        player.append(row)

            # dump the first row of non-player information as well as any rows that may match using list comprehension
        # the code is run twice temporarily until a better script is obtained

    player = [x for x in player if x != player[0]]
    player = [x for x in player if x != player[0]]

        # create a dataframe using the player as data and headings as the column names
    par4_22 = pd.DataFrame(data = player,columns=headers)
    par4_22 = par4_22.drop(columns = ['THIS WEEK','\n                                RANK LAST WEEK'])
        # delete the unecessary columns


    par4_22['par4'] = pd.to_numeric(par4_22['PAR 4 AVG'])

    return par4_22

par4_22 = par4_22()


def par5_22():
    url = 'https://www.pgatour.com/content/pgatour/stats/stat.173.y2022.html'
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text,"lxml")
    category = soup.findAll("table", attrs = {"class" : "table-styled"})

    # scraping the first table
    table1 = category[0]
    # the head will form our column names
    stats = table1.findAll("th",attrs = {"class": ["rank-this","rank-last","player-name","rounds","col-stat"]})

    # Head values (COlumn names) are the first items of the body list
    #header = body[0] #0th item is the header row

    # return the header names of the columns in the first row
    headers = []
    # check the number of headers
    for x in range(len(stats)):
        # check the value count and return their names
        for var in stats[x]:
            headers.append(var)

    headers.pop(0)
    headers[0] = headers[0].text

    body = []

    # find all the rows containing the "tr" element
    # body_rows = soup.find_all("td", attrs = {"class" : ["player-name","hidden-small"]})
    body_rows = soup.find_all("tr")

    # check each page for the element and add the rows into body
    for rows in body_rows:
        body.append(rows)

    player = [] # will be a list for list for all rows

    for row_num in range(len(body)): # a row at a time
        row = [] # this will add old entries for one row
        # use find all in the code below to scrape specifically through the needed tags and avoid a navig/no text error
        for row_item in body[row_num].find_all("td"): # loop through all row entries
                # row_item.text removes the tags from the entries
                # the following regex is to remove \xao and \n and commas from row_item.text
                # the xa0 encodes the flag, \n is the newline and comma separates thousands in numbers
            aa = re.sub("(\xa0)|(\n)|,","",row_item.text)
                # append aa to row - note one row entry is being appended
            row.append(aa)
            # append one row to all_rows
        player.append(row)

            # dump the first row of non-player information as well as any rows that may match using list comprehension
        # the code is run twice temporarily until a better script is obtained

    player = [x for x in player if x != player[0]]
    player = [x for x in player if x != player[0]]

        # create a dataframe using the player as data and headings as the column names
    par5_22 = pd.DataFrame(data = player,columns=headers)
    par5_22 = par5_22.drop(columns = ['THIS WEEK','\n                                RANK LAST WEEK'])
        # delete the unecessary columns


    par5_22['par5'] = pd.to_numeric(par5_22['PAR 5 AVG'])

    return par5_22

par5_22 = par5_22()



# Y22

#page = 1
url = 'https://www.espn.com/golf/stats/player/_/season/2022'
#url = 'https://www.espn.com/golf/statistics/_/year/2022/count/{}'


# have the driver start the browser
driver = webdriver.Chrome(executable_path='C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe')

# retrieve the url
driver.get(url)
time.sleep(2)
#players = soup.findAll("div", attrs = {"class" : "athleteCell__flag flex items-start mr7"})
#res = requests.get(driver.get(url))
#soup = bs4.BeautifulSoup(res.text,"lxml")
#category = soup.findAll("div", attrs = {"class" : "ResponsiveTable ResponsiveTable--fixed-left mt4 Table2__title--remove-capitalization"})


# click the "Show More" button 6 times to display the full amount of data needed

driver.find_element_by_class_name("AnchorLink.loadMore__link").click()
time.sleep(2)
driver.find_element_by_class_name("AnchorLink.loadMore__link").click()
time.sleep(8)
driver.find_element_by_class_name("AnchorLink.loadMore__link").click()
time.sleep(8)
driver.find_element_by_class_name("AnchorLink.loadMore__link").click()
time.sleep(8)
driver.find_element_by_class_name("AnchorLink.loadMore__link").click()
time.sleep(8)
driver.find_element_by_class_name("AnchorLink.loadMore__link").click()
time.sleep(8)




# get the full set of data from the first table on the left

category = driver.find_element_by_class_name("ResponsiveTable.ResponsiveTable--fixed-left.mt4.Table2__title--remove-capitalization")
# athleteCell__flag flex items-start mr7
#soup = bs4.BeautifulSoup(res.text,"lxml")
#category = soup.findAll("div", attrs = {"class" : "ResponsiveTable ResponsiveTable--fixed-left mt4 Table2__title--remove-capitalization"})


# turn the table into legible data
table1 = category.text

# get the left table column heads
headings = table1.split(sep = "\n")[:3]


# get the right table data

stats = driver.find_element_by_class_name('Table__ScrollerWrapper.relative.overflow-hidden')
stats = stats.text

# remove delimiters with space or new lines
kpi = re.split(' |\n',stats)


# get the rightmost table column heads
headers = kpi[:14]


# get the data from the left table

variables = []
for var in (table1.split(sep = "\n")):

    variables.append(var)

df = pd.DataFrame(columns = headings)

driver.quit()


x= 3
y = 4
z = 5

ranks = []
names = []
ages = []


while z < len(variables):

    ranks.append(variables[x])

    names.append(variables[y])


    ages.append(variables[z])

    x = x + 3

    y = y + 3

    z = z + 3

df['RK'] = ranks
df['NAME'] = names
df['AGE'] = ages


e = 16
r = 17
c = 18
t = 19
w = 20
s = 21
d = 22
a = 23
g = 24
p = 25


events = []
rounds = []
cuts = []
t10s = []
wins = []
scores = []
ddis = []
dacc = []
gir = []
putts = []


while p < len(kpi):

    events.append(kpi[e])

    rounds.append(kpi[r])

    cuts.append(kpi[c])

    t10s.append(kpi[t])

    wins.append(kpi[w])

    scores.append(kpi[s])

    ddis.append(kpi[d])

    dacc.append(kpi[a])

    gir.append(kpi[g])

    putts.append(kpi[p])


    e = e + 14
    r = r + 14
    c = c + 14
    t = t + 14
    w = w + 14
    s = s +14
    d = d +14
    a = a +14
    g = g +14
    p = p + 14


df = df.drop(df.index[350:])

df['EVNTS'] = events
df['RNDS'] = rounds
df['CUTS'] = cuts
df['TOP10'] = t10s
df['WINS'] = wins
df['SCORE'] = scores
df['DDIS'] = ddis
df['DACC'] = dacc
df['GIR'] = gir
df['PUTTS'] = putts


df = df.drop(df.index[300:])
y22 = df

#y22 = pd.read_csv(r"y22.csv")
#y22 = pd.read_csv("y22_v2.csv")

y22['Win Rate-C'] =  pd.to_numeric(y22['WINS']) / pd.to_numeric(y22['EVNTS'])
y22['Ten Rate-C'] =  pd.to_numeric(y22['TOP10']) / pd.to_numeric(y22['EVNTS'])


#y22 = y22.drop(["RK"] ,axis = 1)
y22.rename(columns = {'NAME':'PLAYER NAME'}, inplace = True )
y22.rename(columns = {'CUTS':'CUTS MADE-C'}, inplace = True )
y22.rename(columns = {'WINS':'WINS-C'}, inplace = True )
y22.rename(columns = {'TOP10':'TOP10-C'}, inplace = True )
#y22["year"] = 2022


yoy= pd.read_csv(r"yoy.csv")
pr = pd.read_csv(r"proximity.csv")
gr = pd.read_csv(r"greenReg.csv")
dr = pd.read_csv(r"drives.csv")
acc = pd.read_csv(r"accuracy.csv")
par3 = pd.read_csv(r"par3.csv")
par4 = pd.read_csv(r"par4.csv")
par5 = pd.read_csv(r"par5.csv")


# return peak performance by age

y16 = pd.read_csv(r"y16.csv")
#y17["year"] = 2017
#y16['Win Rate'] =  pd.to_numeric(y16['WINS']) / pd.to_numeric(y16['EVNTS'])
#y16['Ten Rate'] =  pd.to_numeric(y16['TOP10']) / pd.to_numeric(y16['EVNTS'])

y17 = pd.read_csv(r"y17.csv")
#y17["year"] = 2017
#y17['Win Rate'] =  pd.to_numeric(y17['WINS']) / pd.to_numeric(y17['EVNTS'])
#y17['Ten Rate'] =  pd.to_numeric(y17['TOP10']) / pd.to_numeric(y17['EVNTS'])

y18 = pd.read_csv(r"y18.csv")
#y18["year"] = 2018
#y18['Win Rate'] =  pd.to_numeric(y18['WINS']) / pd.to_numeric(y18['EVNTS'])
#y18['Ten Rate'] =  pd.to_numeric(y18['TOP10']) / pd.to_numeric(y18['EVNTS'])

y19 = pd.read_csv(r"y19.csv")
#y19["year"] = 2019
#y19['Win Rate'] =  pd.to_numeric(y19['WINS']) / pd.to_numeric(y19['EVNTS'])
#y19['Ten Rate'] =  pd.to_numeric(y19['TOP10']) / pd.to_numeric(y19['EVNTS'])

y20 = pd.read_csv(r"y20.csv")
#y20["year"] = 2020
#y20['Win Rate'] =  pd.to_numeric(y20['WINS']) / pd.to_numeric(y20['EVNTS'])
#y20['Ten Rate'] =  pd.to_numeric(y20['TOP10']) / pd.to_numeric(y20['EVNTS'])

y21 = pd.read_csv(r"y21.csv")
#y21["year"] = 2021
#y21['Win Rate'] =  pd.to_numeric(y21['WINS']) / pd.to_numeric(y21['EVNTS'])
#y21['Ten Rate'] =  pd.to_numeric(y21['TOP10']) / pd.to_numeric(y21['EVNTS'])



y16.rename(columns = {"NAME":"PLAYER NAME"}, inplace = True)
y17.rename(columns = {"NAME":"PLAYER NAME"}, inplace = True)
y18.rename(columns = {"NAME":"PLAYER NAME"}, inplace = True)
y19.rename(columns = {"NAME":"PLAYER NAME"}, inplace = True)
y20.rename(columns = {"NAME":"PLAYER NAME"}, inplace = True)
y21.rename(columns = {"NAME":"PLAYER NAME"}, inplace = True)

y22["slope_w"] = ((y21["WINS"] - y20["WINS"] - y19["WINS"] - y18["WINS"] - y17["WINS"]) / (y21["EVNTS"] - y20["EVNTS"] - y19["EVNTS"] - y18["CUTS"] - y17["EVNTS"])) * -1
y22["slope_10"] = ((y21["TOP10"] - y20["TOP10"] - y19["TOP10"] - y18["TOP10"] - y17["TOP10"]) / (y21["EVNTS"] - y20["EVNTS"] - y19["EVNTS"] - y18["CUTS"] - y17["EVNTS"])) * -1


yoy1 = pd.concat([y21,y20,y19,y18, y17,y16]).groupby(by = "PLAYER NAME", as_index = True)['WINS', 'CUTS', 'TOP10','EVNTS', 'RNDS'].sum()
yoy1["MISS CUTS"] = (yoy1['EVNTS'] - yoy1['CUTS']) * -1

yoy2 = pd.concat([y21,y20,y19,y18, y17,y16]).groupby("PLAYER NAME", as_index = True)['SCORE', 'DDIS', 'DACC', 'GIR', 'PUTTS'].mean()

yoy = pd.concat([yoy1,yoy2]).groupby( by = "PLAYER NAME", as_index = True).sum()


#raw = pd.read_csv(r"/Users/John/Downloads/RAW PGA Histrorical.csv")
raw = pd.read_csv(r"/Users/John/Downloads/RAW PGA Hist.2.csv")

raw.rename(columns = {'player':'PLAYER NAME'}, inplace = True )
df = (raw.pivot_table(index = ['PLAYER NAME']))


prx = pd.concat([pr,prx22]).groupby(by = 'PLAYER NAME', as_index = True).mean()
gr = pd.concat([gr,gr22]).groupby(by = 'PLAYER NAME', as_index = True).mean()
acc = pd.concat([acc,acc22]).groupby(by = 'PLAYER NAME', as_index = True).mean()
par3 = pd.concat([par3,par3_22]).groupby(by = 'PLAYER NAME', as_index = True).mean()
par4 = pd.concat([par4,par4_22]).groupby(by = 'PLAYER NAME', as_index = True).mean()
par5 = pd.concat([par5,par5_22]).groupby(by = 'PLAYER NAME', as_index = True).mean()
dr = pd.concat([dr,dr22]).groupby(by = 'PLAYER NAME', as_index = True).mean()


ytd = pd.merge(yoy,y22, on = ['PLAYER NAME'],how = 'inner')
ytd["WINS"] = pd.to_numeric(ytd["WINS"]) + pd.to_numeric(ytd["WINS-C"])
ytd["CUTS"] = pd.to_numeric(ytd["CUTS"]) + pd.to_numeric(ytd["CUTS MADE-C"])
ytd["MISS CUTS"] = pd.to_numeric(ytd["MISS CUTS"]) + (pd.to_numeric(ytd["EVNTS_y"]) - pd.to_numeric(ytd["CUTS MADE-C"])) * -1
ytd["TOP10"] = pd.to_numeric(ytd["TOP10"]) + pd.to_numeric(ytd["TOP10-C"])
ytd["EVNTS"] = pd.to_numeric(ytd["EVNTS_x"]) + pd.to_numeric(ytd["EVNTS_y"])
ytd["RNDS"] = pd.to_numeric(ytd["RNDS_x"]) + pd.to_numeric(ytd["RNDS_y"])
ytd["SCORE"] = (pd.to_numeric(ytd["SCORE_x"]) + pd.to_numeric(ytd["SCORE_y"])) / 2
ytd["DDIS"] = (pd.to_numeric(ytd["DDIS_x"]) + pd.to_numeric(ytd["DDIS_y"])) / 2
ytd["DACC"] = (pd.to_numeric(ytd["DACC_x"]) + pd.to_numeric(ytd["DACC_y"])) / 2
ytd["GIR"] = (pd.to_numeric(ytd["GIR_x"]) + pd.to_numeric(ytd["GIR_y"])) / 2
ytd["PUTTS"] = (pd.to_numeric(ytd["PUTTS_x"]) + pd.to_numeric(ytd["PUTTS_y"])) / 2

ytd = ytd.drop(['EVNTS_x', 'RNDS_x', 'SCORE_x', 'DDIS_x', 'DACC_x', 'GIR_x', 'PUTTS_x', 'RK', 'EVNTS_y', 'RNDS_y', 'SCORE_y', 'DDIS_y', 'DACC_y', 'GIR_y', 'PUTTS_y'], axis = 1)



gr = gr.drop(['Unnamed: 0'],axis = 1)
par3 = par3.drop(['Unnamed: 0'],axis = 1)
par4 = par4.drop(['Unnamed: 0'],axis = 1)
par5 = par5.drop(['Unnamed: 0'],axis = 1)
dr = dr.drop(['Unnamed: 0'],axis = 1)

carry = pd.concat([prx,acc,gr,dr,par3,par4,par5]).groupby('PLAYER NAME', as_index = True).sum()
carry = carry.drop("Unnamed: 0",axis = 1)

fc = pd.concat([ytd,carry]).groupby('PLAYER NAME', as_index = True).sum()


weather = pd.read_csv("C:\\Users\John\\Desktop\\PGA weather by loc.csv")
weather = weather.drop("Unnamed: 0",axis = 1)
weather.rename(columns = {'player':'PLAYER NAME'}, inplace = True )
weather = weather.sort_values(by = 'pos')
weather = weather[weather.pos != 0]
#weather = weather[weather.pos != 0]
add_ons = pd.DataFrame(data = weather[['PLAYER NAME','win_deg','win_wind','five_deg','five_wind','ten_deg','ten_wind']])
col_means = add_ons[(add_ons != 0).all(1)].mean()
add_ons = add_ons.replace(0, col_means)

add_ons = add_ons.groupby("PLAYER NAME", as_index = True).mean()


raw = pd.read_csv(r"/Users/John/Downloads/RAW PGA Histrorical.csv")
raw.rename(columns = {'player':'PLAYER NAME'}, inplace = True )

raw['date'] = pd.to_datetime(raw['date'], infer_datetime_format=True)
raw['date'] = raw['date'].dt.date

weather['date'] = pd.to_datetime(weather['date'], infer_datetime_format=True)
weather['date'] = weather['date'].dt.date
weather = weather.drop(['city', 'state',
       'weather', 'wind', 'win_deg', 'win_wind', 'five_deg', 'five_wind',
       'ten_deg', 'ten_wind'], axis = 1)

df = pd.merge(raw,weather, on = ['PLAYER NAME', 'tournament name','pos','date'],how = 'inner')
df = (df.pivot_table(index = ['PLAYER NAME','tournament name','pos','date']))


# identify the number of top 10s per location
df['loc t10s'] = raw[raw['pos'] <=10].value_counts(['PLAYER NAME','tournament name'])

# identify the number of top 20s per location
df['loc t20s'] = (raw[raw['pos'] <=20].value_counts(['PLAYER NAME','tournament name']) - df['loc t10s'])


# Remove all the NaN fields
df = df.fillna(0)
#df.sort_values(by = 'm2', ascending = False).head()
#df = df.drop(['year'],axis = 1)
#df.sort_values(by = 'opt_in/outs',ascending= False).head()

# Create Tournament Groups
groups = df.groupby('tournament name')

tournament = "Travelers Championship"
fcast = groups.get_group(tournament)
