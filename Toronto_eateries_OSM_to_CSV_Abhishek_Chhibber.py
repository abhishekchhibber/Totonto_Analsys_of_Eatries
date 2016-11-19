## File#1: This file is used to read and parse the .osm file for Toronto
## The file ouputs a dictonary into a .csv, which has the four attributes: latitude, longitude, amenity, and amenity name (brand name)


import xml.etree.ElementTree as ET
from xml.etree.ElementTree import iterparse
import csv


## Part 1: From .osm to .csv


file = 'toronto_canada.osm'
mainList = [ ]
mainDict = { }
for event, elem in iterparse(file, events=('start', 'end')):

	try:
		tags = elem.findall('tag')
		latPos = elem.attrib['lat']
		mainDict['latitude'] = latPos
		longPos = elem.attrib['lon']
		mainDict['longitude'] = longPos

		for oneTag in tags:
			d = oneTag.attrib['k']
			if d == 'addr:postcode':
				pstcodeValue = oneTag.attrib['v']
				mainDict['postcode'] = pstcodeValue
		for twotag in tags:
			if twotag.attrib['k'] == 'addr:street':
				strAdd = twotag.attrib['v']
				mainDict['street_add'] = strAdd

		mainList.append(mainDict)
		mainDict = { }

	except Exception as e:
		pass

	elem.clear()


## Part 2: Cleaning the .csv for list of eateries

records = [ ]
for row in mainList:
	records.append(row)
print ("Original List length: "+ str(len(records))) # 4894969

filterd = [ ]
desired_amenity = ['bar','cafe','fast_food','ice_cream','pub','restaurant']
for record in records:
	if record['amenity'] in desired_amenity:
		filterd.append (record)
	else:
		pass


## exporting final .csv to be uploaded to MySQL

with open('toronto_eateries.csv', 'w', encoding='utf-8', newline = '') as csvfile: #change here
    fieldnames = ['latitude','longitude','postcode','street_add']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter = ',')
    writer.writeheader()
    for val in filterd:
    	writer.writerow(val)
