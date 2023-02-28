import csv

states = open("states.csv", "r")
rd = csv.reader(states)

statesLines = []

for row in rd:
    statesLines.append(row)

print(statesLines)
