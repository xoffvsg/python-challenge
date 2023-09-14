import os
import csv

election_csv = os.path.join( "Resources", "election_data.csv")      # Identifies the path the the \Resources\election_data.csv file
pollResult={}                                                       # Initialise the dictionary


# with open(udemy_csv, encoding='utf-8') as csvfile:
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")                  # Reads the csv file 
    next(csvreader,None)                                            # Skip the header row
    for row in csvreader:                                           # Starts populating the dictionary with the name of the canditate (key)
        pollResult[row[2]]=pollResult.get(row[2],0)+1               # and count one vote per line. The get method is to avoid an error if
                                                                    # the key does not exist yet.

    #os.system("cls")                                                      # Windows  <--  WILL NEED TO REMOVE BEFORE SUBMITTING if grader is on a MAC   
    print('\n'.join(["",""]))                                              # Skips two lines
    totalCount=0                                                           # Initializes to counter
    print('\n'.join(["Election Results","","------------------",""]))      # Adds spacing and separation line
    for (k,v) in pollResult.items():                                    # Starts reviewing the items in the dictionary k=key and v=value
        totalCount=totalCount+int(v)                                    # and adds up the votes each candidate got to calculate the total
    print(f"Total Votes:   {totalCount}")                               # Prints the total vote count
    print('\n'.join(["","------------------",""]))                          # Adds spacing and separation line
    for (k,v) in pollResult.items():                                    
        percent=int(v)/totalCount                                       # Calculates the % of votes for each candidate
        print(k +":  "+"{:.3%}".format(percent)  +f"  ({v})")           # Diplays the individual results in the order of key creation
        print("")
    print('\n'.join(["------------------",""]))
    print(f"Winner:   {max(pollResult.keys(), key=pollResult.get)}")    # Diplays the name of the winner
    print('\n'.join(["","------------------","","",""]))


