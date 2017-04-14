import csv
import json

with open('countrypopulation.csv') as f:
   reader = csv.DictReader(f)
   rows = list(reader)

with open('newcountries.json', 'w') as f:
   json.dump(rows, f)

