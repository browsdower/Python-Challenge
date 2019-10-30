import os
import csv

#how to define the folder path?
#provide attributes and it will create
csvpath = os.path.join("..", "PyPoll", "election_data.csv")

votes = []
candidate = []
 


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader) 

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        print(row)

        votes.append(row[0])
        
# correy_votes = votes[0]
# o_tooley_votes = votes[0]
# li_votes = votes[0]
# kahn_votes = votes[0]

    for row in csvreader:
        candidate.append(row[2])

    candidate_count = [[x,candidate.count(x)] for x in set(candidate)]
    

    name = []
    
    for row in candidate_count:
        name.append(row[0])
        votes.append(row[1])

    candidate_zip = zip(name, votes)
    candidate_list = list(candidate_zip)

    winner = max(votes)

    for row in candidate_list:
        if row[1] == winner:
            winner_name = row[0]       

#use len to get total amount of votes           
total_votes = len(votes)

correy_total = candidate.count('Correy')
correy_percent = correy_total / total_votes
print(f'Correy Total: {correy_total} with {correy_percent}%')

# o_tooley_total = candidate.count("O'Tooley")
# o_tooley_percent = o_tooley_total / total_votes

# li_total = candidate.count('Li')
# li_percent = li_total / total_votes

# khan_total = candidate.count('Khan')
# khan_percent = khan_total / total_votes

#begin summary headers
print("Total Results:")

#print total votes
print(f'Total Votes: {total_votes}')
print(f'Winner is {winner}')

# Finding the maximum value to determine the winner
# candidate_votes = [correy_votes, o_tooley_votes, li_votes, kahn_votes]
# winner = max(candidate_votes)

# print(f'Winner: {winner}')






# #create empty list for candidates and his/her vote count
# candidates = []
# num_votes = []
# poll = {}

# #takes dictionary keys and values and, respectively, dumps them into the lists, 
# # candidates and num_votes
# for key, value in poll.items():
#     candidates.append(key)
#     num_votes.append(value)

# # creates vote percent list
# vote_percent = []
# for n in num_votes:
#     vote_percent.append(round(n/total_votes*100, 1))

# # zips candidates, num_votes, vote_percent into tuples
# clean_data = list(zip(candidates, num_votes, vote_percent))

# #creates winner_list to put winners (even if there is a tie)
# winner_list = []

# for name in clean_data:
#     if max(num_votes) == name[1]:
#         winner_list.append(name[0])

# # makes winner_list a str with the first entry
# winner = winner_list[0]





 

# total_candidate = [[x,candidate.count(x)] for x in set(candidate)]


# #set variables for each candidate total count
# #set variable to hold percentage won
# correy_votes = candidate.count('Correy')
# correy_percent = correy_votes / total_votes

# o_tooley_votes = candidate.count("O'Tooley")
# o_tooley_percent = o_tooley_votes / total_votes

# li_votes = candidate.count('Li')
# li_percent = li_votes / total_votes

# khan_votes = candidate.count('Khan')
# khan_percent = khan_votes / total_votes








