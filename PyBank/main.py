"""""
Your task is to create a Python script that analyzes the records to calculate each of the following:

  * The total number of months included in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in profits (date and amount) over the entire period

* As an example, your analysis should look similar to the one below:

"""""

import os
import csv
from typing import TYPE_CHECKING
#print (budget_data)
budget_data = os.path.join("Resources" , "budget_data.csv")

#send to text file
text_file = os.path.join("budgetdata.txt")
  
#variables
totalMonths = 0
net_changes = [] 
total_Profits_Losses = 0
date_changes = []
total_net_profit = 0
month_changes = []
dates = []

#read csv file
with open(budget_data) as budget_data:
    csvreader = csv.reader(budget_data)

#header row    
    date = next(csvreader)



    #move to first row of dates and profits
    first_row = next(csvreader)

    #establish previous revenue
    totalMonths = totalMonths + 1
    total_net_profit += int(first_row[1])

    prev_net_profit = int(first_row[1])
    total_Profits_Losses += float(first_row[1])

    #previous_row = float(first_row[1])

    

    for row in csvreader:
        totalMonths += 1
        total_net_profit += int(row[1])
        
        net_change = int(row[1]) - prev_net_profit
        net_changes.append(net_change)
        month_changes.append(row[0])

        dates.append(row[0])
        
        prev_net_profit = int(row[1])

        #profit_changes = int(row[1]) - previous_row
        
        #previous_row = int(row[1])


    
    #total_Profits_Losses += 1
    
    #for row in csvreader:
        #total_Profits_Losses += 1


#print(net_changes)
date = f"Total Months = {totalMonths} "
print(date) 

Profits_Losses = f"Total Profits and Losses = {total_Profits_Losses} "
print(Profits_Losses)

avg_profit_change = sum(net_changes) / len(net_changes)
profit_change = f"Average Profit Change = {avg_profit_change} "
print(profit_change)

largest_increase = [dates[0],net_changes[0]]
largest_decrease = [dates[0],net_changes[0]]

for m in range(len(net_changes)):
  if (net_changes[m] > largest_increase[1]):
    largest_increase[1] = net_changes[m]
    largest_increase[0] = dates[m]

  if (net_changes[m] < largest_decrease[1]):
    largest_decrease[1] = net_changes[m]
    largest_decrease[0] = dates[m]



print(f"Largest Increase = {largest_increase}, Largest Decrease = {largest_decrease}")
#print (f"Profit Changes over Time = {profit_changes}")
#total_profit_changes = statistics.fmean(profit_changes)
#print (total_profit_changes)
#avg_profit = sum(profit_changes) / len(profit_changes)
#print(avg_profit)

with open(text_file, "w") as textfile:
  textfile.write(date)
  textfile.write(Profits_Losses)
  textfile.write(profit_change)
  #textfile.write(largest_increase)
  #textfile.write(largest_decrease)
