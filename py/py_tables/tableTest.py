from prettytable import PrettyTable
from tables import * 
import json

f = open("test.json")

data = json.load(f)
functionNames = [function['function'] for function in data['functions']]
inputValues = [function['input'] for function in data['functions']]
processingValues = [function['processing'] for function in data['functions']]
outputValues = [function['output'] for function in data['functions']]

# print([functionName for functionName in functionNames])

table_header_rows = ["Input", "Processing", "Output", ]
dashes = []
for header in table_header_rows: dashes.append("-" * len(header)) 

for i in range(len(functionNames)):
    table = PrettyTable()
    table.add_column("", "", "c")
    table.add_column(functionNames[i], "", "c")
    table.add_column("", "", "c")
    table.add_row(table_header_rows[i])
    table.add_row(dashes[i])
    table.add_row(inputValues[i], processingValues[i], outputValues[i])
    print(table)

# for header in table_header_rows: table.add_row(header)



# print("{:*^57s}".format(function_names[0]))
# for alignment in range(len(table_header_rows)):
#     align ="{:"+ (table_header_rows[alignment])[0:1]+"24s}"
#     print(align.format(( [header_row[1:] for header_row in table_header_rows])[alignment]), end="")


