import os
import csv
#how to define the folder path?
#provide attributes and it will create
csvpath = os.path.join("..", "PyBank", "budget_data.csv")

print(csvpath)

# with open(budget_data.csv, newline="") as csvpath:
#     csv_reader = csv.reader(csvpath, delimiter=",")



#     csv_header = next(csv_reader)
#     print(f"CSV Header: {csv_header}")

#     for row in csvreader:
#         print(row)
