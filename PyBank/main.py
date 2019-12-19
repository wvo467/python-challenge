import os
import csv

#Set variables 
total_months = 0
total_revenue = 0
avg_changes = []
greatest_increase = 0
greatest_decrease = 0

#Open csv
csvpath = os.path.join("..", "Resources", "budget_data.csv")

with open(csvpath, newline=" ") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreaderm None)

#Calculate total months and rev
