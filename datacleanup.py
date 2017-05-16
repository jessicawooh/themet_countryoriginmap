#import csv
newcsv=open("countrypopulation.csv", "w")
#mywriter=csv.writer(newcsv, delimiter = ",")
listOfcountries=open("listOfcountries.txt","r")
countriesfile=open("MetObjectsCountries.txt","r")
countries = []
countries = countriesfile.readlines()
index=[]

#print "countries length=" + str(len(countries))


for row in listOfcountries:
		rowcount = 0 
		#debugging
		#print "row = " + row
		#print "initrowcount = " + str(rowcount)
		for country in countries:
			#debugging
			#print str(row) + ': ' + country + '\n'
			if str(row) in str(country):
					rowcount += 1
			#debugging		
			#print "final rowcount =" + str(rowcount)
		index.append(row.strip('\n') + "," + str(rowcount))

#for item in index:
	#print item
#for item in index:
#		mywriter.writerow(item)
newcsv.write("name,population" + "\n")
for item in index:
	newcsv.write(item + "\n")
