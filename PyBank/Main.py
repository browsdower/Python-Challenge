import os
import csv
#follow path, then method, then folder, then file name
csvpath = os.path.join("..", "PyBank", "budget_data.csv")

#create variables to hold month and revenue totals
months = []
revenue = []

#run open and read file with header
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader) 

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

#format csv data into list format
    for row in csvreader:
        print(row)

        months.append(row[0])
        revenue.append(int(row[1]))

#begin summary output
print("Financial Analysis:")

#use len to get the total count of a column
total_months = len(months)
print(f'Total Months: {total_months}')

#define variables for increase, decrease and total revenue amounts
greatest_increase = revenue[0]
greatest_decrease = revenue[0]
total_revenue = 0

#set loop for revenue, total revenue
#compare revenue to find greatest increase and decrease
#add revenue to total revenue
for r in range(len(revenue)):
    if revenue[r] >= greatest_increase:
        greatest_increase = revenue[r]
        great_inc_month = months[r]
    elif revenue[r] <= greatest_decrease:
        greatest_decrease = revenue[r]
        great_dec_month = months[r]
    total_revenue += revenue[r]

#final print commands for summary 
print(f'Greatest Decrease ${greatest_decrease}')

print(f'Greatest Decrease Month {great_dec_month}')

print(f'Greatest Increase ${greatest_increase}')

print(f'Greatest Increase Month {great_inc_month}')

print(f'Total ${total_revenue}')
