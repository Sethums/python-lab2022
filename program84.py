import csv
with open('abc.txt') as inf:
 content = csv.DictReader(inf)

 print("Name")

 for row in content:
   print(row["Name"])
    
