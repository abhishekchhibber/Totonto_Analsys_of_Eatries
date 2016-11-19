# Totonto_Analsys_of_Eatries
##This project analyzes all the restaurants, pubs, fast food joints, and cafes in Toronto, Canada
### Stack Used: Python (3.5), MySQL, Javascript (for query tool), iPython (for analysis)

This project lists all the eateries in the city of Toronto, Canada. It helps end user to type-in their postal code and get a list of all the restaurants, pubs, cafes, and fastfood joints in the given postal code.

I have used the data from [Open Street Map](https://www.openstreetmap.org/) and used the following steps to clean, analyze and present it. 

##Steps Involved

* I downloaded the. osm file for Toronto from [mapzen](https://mapzen.com/data/metro-extracts/metro/toronto_canada/).
  * The compressed (.bz2) file is 79.2 MB in size, while the uncompressed (.osm) file is 1.15 GB in size.
* Once I had the. osm file on Toronto, I parsed it using Iterparse (Elemettree) to extract the following four things:
  * Latitude
  * Longitude
  * Amenity (e.g. fast_food)
  * Amenity Name (e.g. McDonald's)
* The .csv file generated from the previous step had a size of approximately 120 MB, as it had all the latitudes and longitudes mentioned in the. osm file. Therefore, I filtered out only the results, where the field ‘amenity’ was not null, and finally filtered out the results for amenities = eateries. 
* Once I had the latitudes, logitudes, eateries, and their names, I used [Google's reverse geocoding](https://developers.google.com/maps/documentation/javascript/examples/geocoding-reverse) and parsed postal codes for all the eateries. 

 
