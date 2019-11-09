import csv
import math
from math import *
from csv import reader


opened_file = open(r'C:\users\aj\downloads\salaries_bb.csv')
read_file = reader(opened_file)
salaries = list(read_file)
salaries_header = salaries[:1]
salaries = salaries[1:]

 
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

players_with_5x = []
for row in players_playing:
	salary_x5 = (float(row[4])/1000) * 5
	row[7] = str(salary_x5)
	players_with_5x.append(row)



## Replaces one of the unused columns in the table with a simple standard deviation calculation taken from the cieling and floor values.
players_with_std_dev = []
for row in players_with_5x:
	std_dev = (float(row[10])-float(row[11])) / 2
	row[6] = str(std_dev)
	players_with_std_dev.append(row)

##isolates only the skaters (non-goalies) who have a standard deviation of over 5 and that are on the powerplay lines
players_with_high_floors = []
for row in players_with_std_dev:
	if (float(row[6]) < 13.5):
		players_with_high_floors.append(row)


##eliminates the brackets and quotes from printed .csv output
for row in salaries_header:
	b = ",".join(row)
	print(b, "\n")
for row in players_with_high_floors:
	b = ",".join(row)
	print(b, "\n")


## prints the results to a .csv file

with open('out_bb_cash.csv', 'w', newline="") as f:
	writer = csv.writer(f)
	writer.writerows(salaries_header)
	writer.writerows(players_with_high_floors)