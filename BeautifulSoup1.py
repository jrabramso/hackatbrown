from bs4 import BeautifulSoup

import requests
import json

r  = requests.get("http://brown.cafebonappetit.com/cafe/sharpe-refectory/")

data = r.text

soup = BeautifulSoup(data, "lxml")

#for link in soup.find_all('collard greens'):
 #   print()
    
#letters = soup.find_all("section id=", sectionid_="panel-daypart-menu-1")

soup2 = soup.find_all("section", class_="panel panel-type-daypart panel-even")
#print soup2


#print soup2.find("Bamco.menu_items")


soupString = str(soup2)
splitString = soupString.split("Bamco.menu_items = ")
splitAgain = splitString[-1].split("Bamco.cor_icons")

#print splitAgain[0]
jsonFile = splitAgain[0][0:-11]

json = json.loads(jsonFile)

itemsList = []

for key in json.keys():
    json1 = json[key]
    for key1 in json1:
        if key1 == "label":
            itemsList.append(json1[key1])

print itemsList