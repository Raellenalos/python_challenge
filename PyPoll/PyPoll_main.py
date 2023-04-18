
#Import Libraries
import os
import csv


#Point to file
poll_csv = os.path.join('Resources', 'election_data.csv')

#Declare variables
candidates = set()
candidate_list = []
total_votes = 0
candidate_count = [0,0,0]
charles_casper = 0
charles_percent = 0.0
diana_degette = 0
diana_percent =0.0
raymon_doane = 0
raymon_percent = 0.0

#Open file 
with open(poll_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    #Create Header
    header= next(csv_reader)   
    
    #Loop through rows
    for row in csv_reader:
        
        #Count the nuber of votes
        total_votes += 1
        
       
        #Add votes
        if row[2] == "Charles Casper Stockham": 
            candidate_count[0] += 1
        elif row[2] == "Diana DeGette":
            candidate_count[1] += 1
        elif row[2] == "Raymon Anthony Doane": 
            candidate_count[2] += 1
            
        if (row[2] in candidates):
            continue
        candidates.add(row[2])
        candidate_list.append(row)

    #Percentage of vote for each candidates
    charles_percent = candidate_count[0] / total_votes
    diana_percent = candidate_count[1] / total_votes
    raymon_percent = candidate_count[2] / total_votes

    #Find the winner
    if candidate_count[0] > candidate_count[1] and  candidate_count[0] > candidate_count[2]:
        winner = "Charles Casper Stockham"
    elif candidate_count[1] > candidate_count[0] and  candidate_count[1] > candidate_count[2]:
        winner = "Diana DeGette"
    elif candidate_count[2] > candidate_count[1] and  candidate_count[2] > candidate_count[0]:
        winner = "Raymon Anthony Doane"
    else:
        winner = "No One Won"
    
    #Print Commands
    print("\nElection Analysis Results\n")
    print("---------------------------\n")
    #* The total number of votes cast
    print(f'Total Votes: {str(total_votes)}')
    print("---------------------------\n")
    
    #* A complete list of candidates who received votes
    print(f'This is the list of candidates:\n {candidates}\n')
    
    #* The percentage of votes each candidate won and the total number of votes each candidate won
    print(f'Charles Casper Stockham:{charles_percent:,.3%} ({candidate_count[0]})\n')
    print(f'Diana DeGette: {diana_percent:,.3%} ({candidate_count[1]})\n')
    print(f'Raymon Anthony Doane: {raymon_percent:,.3%} ({candidate_count[2]})\n')
    
    #* The winner of the election based on popular vote.
    print(f'Winner : {winner}')

#we will use to establish where is txt file will go to
output_file = os.path.join("analysis","poll_analysis_results.txt")

with open(output_file, 'w') as txt_file:
    txt_file.write("ElectionAnalysisResults\n")
    txt_file.write("\n---------------------------\n")
    #* The total number of votes cast
    txt_file.write(f'Total Votes: {str(total_votes)}\n')
    txt_file.write("\n---------------------------\n")
    
    #* A complete list of candidates who received votes
    txt_file.write(f'\nCandidates list:\n {candidates}\n')
    
    #* The percentage of votes each candidate won and the total number of votes each candidate won
    txt_file.write(f'\nCharles Casper Stockham:{charles_percent:,.3%} ({candidate_count[0]})\n')
    txt_file.write(f'Diana DeGette: {diana_percent:,.3%} ({candidate_count[1]})\n')
    txt_file.write(f'Raymon Anthony Doane: {raymon_percent:,.3%} ({candidate_count[2]})\n')
    
    #* The winner of the election based on popular vote.
    txt_file.write(f'\nWinner!!! : {winner}')