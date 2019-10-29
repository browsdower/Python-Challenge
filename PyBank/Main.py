import os
import csv
#how to define the folder path?
#provide attributes and it will create
csvpath = os.path.join("..", "PyBank", "budget_data.csv")

months = []
revenue = []

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader) 

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")


    for row in csvreader:
        print(row)

        months.append(row[0])
        revenue.append(int(row[1]))


total_months = len(months)
print(total_months)