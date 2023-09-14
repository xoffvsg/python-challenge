import os
import csv

election_csv = os.path.join( "Resources", "election_data.csv")
pollResult={}


# with open(udemy_csv, encoding='utf-8') as csvfile:
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader,None)
    for row in csvreader:
        pollResult[row[2]]=pollResult.get(row[2],0)+1

    #print(list(pollResult))
    print(list(pollResult.items()))
        

