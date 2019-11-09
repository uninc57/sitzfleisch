import math
import csv
from math import *
from csv import reader


opened_file = open(r'C:/users/aj/downloads/hockey.csv')
read_file = reader(opened_file)
salaries = list(read_file)
salaries_header = salaries[:1]
salaries = salaries[1:]

##renaming columns that aren't used into something that will be to keep the spreadsheet small 
for col in salaries_header:
	col[6] = str("Standard Deviation")
	col[7] = str("5x of Salary")
	col[9] = str("Chance of 5x")


## makes a list of only players who are playing that night (or have projections)
players_playing = []
players_not_playing = []
for row in salaries:
	projected = float(row[5])
	if projected > 0:
		players_playing.append((row))
	else:
		players_not_playing.append(row)
## divides salary by 1000 then multiplies by 5 to get a target score

players_with_5x = []
for row in players_playing:
	salary_x5 = (float(row[4])/1000) * 3
	row[7] = str(salary_x5)
	players_with_5x.append(row)



## Replaces one of the unused columns in the table with a simple standard deviation calculation taken from the ceiling and floor values.
players_with_std_dev = []
for row in players_with_5x:
	std_dev = (float(row[10])-float(row[11])) / 2
	row[6] = str(std_dev)
	players_with_std_dev.append(row)


## isolates the starting goalies, as they do not have a line or powerplay line assigned and need to be factored out before the rest of the program runs
goalies = []
for row in players_with_std_dev:
	if row[2] == "G":
		goalies.append(row)

##isolates only the skaters (non-goalies) who have a standard deviation of over 5 and that are on the powerplay lines
players_with_high_ceilings = []
for row in players_with_std_dev:
	if (float(row[6]) < 10) and (int(row[14]) > 0):
		players_with_high_ceilings.append(row)

##creates lists of the remainig postitions that meet the prior criteria
wings = []
centers = []
defense = []
for row in players_with_high_ceilings:
	if  row[2] == "LW" or row[2] == "RW":
		wings.append(row)
	elif row[2] == 'C':
		centers.append(row)
	elif row[2] == 'D':
		defense.append(row)

##eliminates the brackets and quotes from printed .csv output
for row in salaries_header:
	b = ",".join(row)
	print(b, "\n")
for row in wings:
	b = ",".join(row)
	print(b, "\n")

for row in centers:
	b = ",".join(row)
	print(b, "\n")

for row in defense:
	b = ",".join(row)
	print(b, "\n")

for row in goalies:
	b = ",".join(row)
	print(b, "\n")



## prints the results to a .csv file

with open('out_cash.csv', 'w', newline="") as f:
	writer = csv.writer(f)
	writer.writerows(salaries_header)
	writer.writerows(wings)
	writer.writerows(centers)
	writer.writerows(defense)
	writer.writerows(goalies)