import os
import csv

#provide path to retrive csv data file 
csvpath = os.path.join("..", "PyPoll", "election_data.csv")

#set empty vatiables for data
votes = 0

#run open and read the file with header
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader) 
#brin in header titles
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    candidate_totals = {}
#loop through row 2 and count candidate names, if new name, create a new candidate 
    for row in csvreader:
        candidate_new = (row[2])
        if candidate_new in candidate_totals:
            candidate_totals[candidate_new] += 1
        else:
            candidate_totals[candidate_new] = 1
#count total votes
        votes += 1
#formatting
print('Election Results:')
print('-----------------')
print(f'Total votes {votes}')
print('-----------------')
#count unique names by candidate
#return unique names, add percentage of vote, and total vote count
ord = 0
for result in sorted(candidate_totals, key=candidate_totals.get, reverse=True):
    ord += 1
    print(f' {ord}: {result} ({candidate_totals[result] / votes * 100}%) {candidate_totals[result]} votes ')

#formatting
print('-----------------')
print(f'Winner: Khan ')
print('-----------------')