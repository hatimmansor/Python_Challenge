# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('.','Resources','budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

  

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    
    
    # initialize all the variables that required in this task   
    Total_Months=0
    Total=0
    Average_change=0
    Increase=0
    Decrease=0
    Previous_cell_value=0
    changes=0
    
    # Read each row of data after the header
    for row in csvreader:
        Total_Months+=1
        Total+=int(row[1])
        temp=int(row[1])
        if Total_Months!=1:
            changes+=temp-Previous_cell_value
    
    #check for the greatest increase in ptofits
        if (temp>Increase):
            Increase=temp-Previous_cell_value
            Inc_Month=row[0]
    
    #check for the greatest decrease in ptofits
        if (temp<Decrease):
            Decrease=temp-Previous_cell_value
            Dec_Month=row[0]
        Previous_cell_value=temp

    #generate the printed message
    Table_print=f"Financial Analysis \n\
------------------------\n\
Total Months: {Total_Months}\n\
Total: ${Total}\n\
Average Change= ${changes/(Total_Months-1)}\n\
Createst Increase in profits: {Inc_Month} (${Increase})\n\
Createst Decrease in profits: {Inc_Month} (${Decrease})"
    print(Table_print)

    #Write to results to results.txt
    Results_path = os.path.join('.','analysis','reuslts.txt')

    with open(Results_path, "w") as txt_file:
        txt_file.write(Table_print)

