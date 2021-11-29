# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('pypoll','Resources','election_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

  

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    
    
    # initialize all the variables that required in this task   
    Total_Votes=0
    Candidates_list=[]
    Candidate_votes=[]
    
    
    # Read each row of data after the header
    for row in csvreader:
        Total_Votes+=1
        if row[2] not in Candidates_list:
            Candidates_list.append(row[2])
            Candidate_votes.append(int(0))
        
        
        Candidate_votes[Candidates_list.index(row[2])]+=1

    Final_results=zip(Candidates_list,Candidate_votes)
    # Using sorted and lambda
    Final_results= sorted(Final_results, key = lambda x: x[1],reverse=True)
  
  
    #generate the printed message
    Table_print=f"Election Results\n\
-------------------------\n\
Total Votes: {Total_Votes}\n\
-------------------------\n"

    for x in Final_results:
        Table_print+=f"{x[0]}: {x[1]/Total_Votes:.3%} ({x[1]})\n"
    Table_print+=f"-------------------------\n\
Winner: {Final_results[0][0]}\n\
-------------------------"

    print(Table_print)

    #Write to results to results.txt
    Results_path = os.path.join('pyPoll','analysis','reuslts.txt')

    with open(Results_path, "w") as txt_file:
        txt_file.write(Table_print)

