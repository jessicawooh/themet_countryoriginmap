import csv
import json

with open('MetObjects.csv') as f:
   reader = csv.DictReader(f)
   rows = list(reader)

with open('MetObjects.json', 'w') as f:
   json.dump(rows, f)

