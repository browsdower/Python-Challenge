import os
import csv


#provide path to retrive csv data file 
csvpath = os.path.join("..", "PyPoll", "election_data.csv")

#set empty vatiables for data
votes = []
# candidate_name = []
# candidate_votes = []
 
#run open and read the file with header
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader) 

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    candidate_totals = {}

    for row in csvreader:
        candidate_new = (row[2])
        if candidate_new in candidate_totals:
            candidate_totals[candidate_new] += 1
        else:
            candidate_totals[candidate_new] = 1

    for candidate_name, total in candidate_totals.items():
        print(f'candidate {candidate_name} received {total} votes')


        
print(f'Total votes {votes}')
print(f'Each candidate : {candidate_totals}')

ord = 0
for result in sorted(candidate_totals, key=candidate_totals.get, reverse=True):
    ord += 1
    print(f'Candidate # {ord}: {result} with {candidate_totals[result]} votes ({candidate_totals[result] / votes * 100}%)')

# total_votes = len(votes)
# print(f'Total Votes: {total_votes}')

#  # Find the winning candidate
# winner = max(total)
# print(f'Winnter: {winner}')


    # for row in csvreader:
    #     print(row)

    #     votes.append(int(row[0]))











# #     csv_header = next(csvreader)
# #     print(f"CSV Header: {csv_header}")

# candidates = []

# # A list to capture the number of votes each candidate receives
# num_votes = []

# # A list to capture the percentage of total votes each candidate garners 
# percent_votes = []

# # A counter for the total number of votes 
# total_votes = 0

# # with open(election_data, newline = "") as csvfile:
# #     csvreader = csv.reader(csvfile, delimiter = ",")
# #     csv_header = next(csvreader)

#     for row in csvreader:
#     # Add to our vote-counter 
#         total_votes += 1 

       
#         if row[2] not in candidates:
#             candidates.append(row[2])
#             index = candidates.index(row[2])
#             num_votes.append(1)
#         else:
#             index = candidates.index(row[2])
#             num_votes[index] += 1
    
#     # Add to percent_votes list 
#     for votes in num_votes:
#         percentage = (votes/total_votes) * 100
#         percentage = round(percentage)
#         percentage = "%.3f%%" % percentage
#         percent_votes.append(percentage)
    
#     # Find the winning candidate
#     winner = max(num_votes)
#     index = num_votes.index(winner)
#     winning_candidate = candidates[index]

# # Displaying results
# print("Election Results")
# print("--------------------------")
# print(f"Total Votes: {str(total_votes)}")
# print("--------------------------")
# for i in range(len(candidates)):
#     print(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
# print("--------------------------")
# print(f"Winner: {winning_candidate}")
# print("--------------------------")





# # candidate_totals = {}

# # for row in csvreader:
# #     candidate_new = (row[2])
# #     if candidate_new in candidate_totals:
# #         candidate_totals[candidate_name] += 1
# #     else:
# #         candidate_totals[candidate_name] = 1

# # print(f'Total votes {votes}')
# # print(f'Each candidate: {candidate_totals}')


# # # pct = []
# # # max_votes = candidate_votes[0]
# # # max_index = 0

# # # for x in range(len(candidate_name)):
# # #     #calculation to get the percentage, x is the looper value
# # #     vote_pct = round(candidate_votes[x]/votes*100, 2)
# # #     pct.append(vote_pct)
    
# # #     if candidate_votes[x] > max_votes:
# # #         max_votes = candidate_votes[x]
# #         max_index = x

# election_winner = candidate_name[max_index] 

# print(f'Vote count for each candidate: {candidate_votes}')
# print(f'Max votes: {max_votes}')
# print(f'Election winner: {election_winner}')

# for x in range(len(candidate_name)):
#     print(f'{candidate_name[x]} : {pct[x]}% ({candidate_votes[x]})')



# #format csv data into list
# #     for row in csvreader:
# #         print(row)

# #         votes.append(row[0])
        
# # # correy_votes = votes[0]
# # # o_tooley_votes = votes[0]
# # # li_votes = votes[0]
# # # kahn_votes = votes[0]

# #     for row in csvreader:
# #         candidate.append(row[2])

# # candidate_list = []

# # candidate_names = ["Correy", "O_Tooley", "Li", "Kahn"]

# # candidate_list.append(candidate_names + 1)


# # def countLi(csvreader, Li): 
# #     return lst.count(Li) 
  
# # # Driver Code 
# # lst = [8, 6, 8, 10, 8, 20, 10, 8, 8] 
# # x = 8
# # print(f''

#     # name = []
    
#     # for row in candidate_count:
#     #     name.append(row[0])
#     #     votes.append(row[1])

#     # candidate_zip = zip(name, votes)
#     # candidate_list = list(candidate_zip)

#     # winner = max(votes)

#     # for row in candidate_list:
#     #     if row[1] == winner:
#     #         winner_name = row[0]       



# # correy_total = candidate_list.count('Correy')
# # correy_percent = correy_total / total_votes
# # print(f'Correy Total: {correy_total} with {correy_percent}%')

# # o_tooley_total = candidate.count("O'Tooley")
# # o_tooley_percent = o_tooley_total / total_votes

# # li_total = candidate.count('Li')
# # li_percent = li_total / total_votes

# # khan_total = candidate.count('Khan')
# # khan_percent = khan_total / total_votes


# #use len to get total amount of votes           
# # total_votes = len(votes)

# #begin summary headers
# print("Total Results:")

# #print total votes
# # print(f'Total Votes: {total_votes}')
# # print(f'Winner is {winner}')

# # Finding the maximum value to determine the winner
# # candidate_votes = [correy_votes, o_tooley_votes, li_votes, kahn_votes]
# # winner = max(candidate_votes)

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








