import json
metObjects=[]
with open('MetObjects.json') as jsondata:
	metObjects=json.load(jsondata)

numberOfCountries=dict()
for object in metObjects:
	if object['Country'] in numberOfCountries:
		numberOfCountries[object['Country']] += 1
	else:
		numberOfCountries[object['Country']] = 1

countries = []

for key,value in numberOfCountries.items():
	country=dict()
	country['name']=key
	country['population']=value 
	countries.append(country)



print json.dumps(countries)
