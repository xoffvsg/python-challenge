import os
import csv

budget_csv_path = os.path.join( "Resources", "budget_data.csv")      # Identifies the path to the \Resources\budget_data.csv file


# with open(udemy_csv, encoding='utf-8') as csvfile:
with open(budget_csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")                  # Reads the csv file 
    next(csvreader,None)                                            # Skip the header row

    budget=[]                                                       # Initialise the list   
    for row in csvreader:                                           # Starts populating the list with a nested list of three values
        budget.append([row[0],float(row[1]),0])                     # Note: could have used INT instead of FLOAT but this is more universal

    months=len(budget)                                              # Finds the number of months by assessing the length of the list
    
    for i in range(1,months):
        budget[i][2]=budget[i][1]-budget[i-1][1]                    # Calculates the change month-to-month and stores it in the 

    netTotal=0                                                      # Initialise the variables
    netChange=0
    for i in range(months):
        netTotal=netTotal+budget[i][1]                              # Calculates the various totals
        netChange=netChange+budget[i][2]
    aveChange=netChange/(months-1)                                  # Calculates the average. n-1 because the first month is empty
    maxVal=max(budget, key=lambda x: x[2])      #https://www.geeksforgeeks.org/python-find-the-sublist-with-maximum-value-in-given-nested-list/
    minVal=min(budget, key=lambda x: x[2])                          # Finds the max/min in a nested list. Returns the full list for the corresponding index

#_______________________________________________________________    Display the output to the terminal
    print('\n'.join(["",""]))                                               # Skips two lines
    print('\n'.join(["Financial Analysis","","------------------",""]))     # Adds spacing and separation line
    print(f"Total Months:   {months}"+"\n")                                 # Prints the total month count
    print("Total :  "+"${:.0f}".format(netTotal)+"\n")                      # Prints the net total amount of Profit/Losses
                                                                            # needs to adjust the format since the type is FLOAT and not INT
    print("Average Change:  "+"${:.2f}".format(aveChange)+"\n"+"\n")        # Diplays the average change with some spacing
    print(f"Greatest Increase in Profits: {maxVal[0]}"  +"  (${:.0f}".format(maxVal[2])+")\n")     
    print(f"Greatest Decrease in Profits: {minVal[0]}" +"   (${:.0f}".format(minVal[2])+")\n"+"\n"+"\n")    


#__________________________________________________________________  Output results to a text file in a subdirectory named "analysis"

output_path = os.path.join("analysis","financial_results.txt")       # Identifies the path to the \analysis\financial_results.txt file to be created

with open(output_path, "w", newline='') as datafile:                # Creates the file 
    datafile.write('\n'.join(["",""]))                                               # Skips two lines
    datafile.write('\n'.join(["Financial Analysis","","------------------","\n"]))     # Adds spacing and separation line
    datafile.write(f"Total Months:   {months}"+"\n"+"\n")                                 # Prints the total month count
    datafile.write("Total :  "+"${:.0f}".format(netTotal)+"\n"+"\n")                      # Prints the net total amount of Profit/Losses
                                                                            # needs to adjust the format since the type is FLOAT and not INT
    datafile.write("Average Change:  "+"${:.2f}".format(aveChange)+"\n"+"\n")        # Diplays the average change with some spacing
    datafile.write(f"Greatest Increase in Profits: {maxVal[0]}"  +"  (${:.0f}".format(maxVal[2])+")\n"+"\n")     
    datafile.write(f"Greatest Decrease in Profits: {minVal[0]}" +"   (${:.0f}".format(minVal[2])+")\n"+"\n"+"\n")  
    datafile.close()                                                # Close the file     
