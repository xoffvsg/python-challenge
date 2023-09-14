import os
import csv

election_csv_path = os.path.join( "Resources", "election_data.csv")      # Identifies the path to the \Resources\election_data.csv file


# with open(udemy_csv, encoding='utf-8') as csvfile:
with open(election_csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")                  # Reads the csv file 
    next(csvreader,None)                                            # Skip the header row
    
    pollResult={}                                                   # Initialise the dictionary   
    for row in csvreader:                                           # Starts populating the dictionary with the name of the canditate (key)
        pollResult[row[2]]=pollResult.get(row[2],0)+1               # and count one vote per line. The get method is to avoid an error if
                                                                    # the key does not exist yet.


#_________________________________________________________________  Output results to the terminal

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
        print("")                                                           # Adds spacing
    
    print('\n'.join(["------------------",""]))                             # Adds spacing and separation line
    print(f"Winner:   {max(pollResult.keys(), key=pollResult.get)}")    # Diplays the name of the winner
    print('\n'.join(["","------------------","","",""]))                    # Adds spacing and separation line


#__________________________________________________________________  Output results to a text file in a subdirectory named "analysis"

output_path = os.path.join("analysis","election_results.txt")       # Identifies the path to the \analysis\election_results.txt file to be created

with open(output_path, "w", newline='') as datafile:                # Creates the file
   
    datafile.write("\n")                                            # Adds spacing. Note the "\n" is here necessary, while "" was sufficient in the terminal
    datafile.write('\n'.join(["Election Results","\n","------------------","\n"]))
    datafile.write(f"Total Votes:   {totalCount}"+"\n"+"\n"+"------------------"+"\n"+"\n")
    
    for (k,v) in pollResult.items():                                    
        percent=int(v)/totalCount                                                 # Calculates the % of votes for each candidate
        datafile.write(k +":  "+"{:.3%}".format(percent)  +f"  ({v})"+"\n"+"\n")  # Diplays the individual results in the order of key creation
        
    datafile.write('\n'.join(["------------------","\n"]))                             # Adds spacing and separation line
    datafile.write(f"Winner:   {max(pollResult.keys(), key=pollResult.get)}")    # Diplays the name of the winner
    datafile.write('\n'.join(["\n","------------------","\n","\n","\n"]))              # Adds spacing and separation line
    datafile.close()                                                # Close the file


