import os
import csv

csvpath = os.path.join("..", "Resources", "budget_data.csv")

with open(csvpath, newline=" ") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    