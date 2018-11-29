import os
import csv
import subprocess

with open("usable_data.csv", 'r') as csvfile:  #reading a csv of one column of only urls
    file = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in file:
        row = str(row)
        row = row.rstrip("[]'") #taking away extra characters from the left and right
        row = row.lstrip("[]'")
        #print(row)
        subprocess.run(args=['nslookup',row], capture_output=True) #this is how you run commang line arguments
        #print(subprocess.CompletedProcess.stdout)

        #str(row)