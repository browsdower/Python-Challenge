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

greatest_inc = revenue[0]
greatest_dec = revenue[0]
total_revenue = 0

#loop through revenue and compare to find greatest inc and dec
#add revenue to total revenue
for r in range(len(revenue)):
    if revenue[r] >= greatest_inc:
        greatest_inc = revenue[r]
        great_inc_month = months[r]
    elif revenue[r] <= greatest_dec:
        greatest_dec = revenue[r]
        great_dec_month = months[r]
    total_revenue += revenue[r]

print(f'Greatest Decrease ${greatest_dec}')

print(f'Greatest Decrease Month {great_dec_month}')

print(f'Greatest Increase ${greatest_inc}')

print(f'Greatest Increase Month {great_inc_month}')

print(f'Total ${total_revenue}')
