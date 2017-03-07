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
print json.dumps(numberOfCountries)
