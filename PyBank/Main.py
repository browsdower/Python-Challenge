import os
import csv
#how to define the folder path?
#provide attributes and it will create
csvpath = os.path.join("..", "PyBank", "budget_data.csv")


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader) 

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        print(row)
