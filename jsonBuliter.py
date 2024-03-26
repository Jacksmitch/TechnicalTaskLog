# Created By Jackson Mitchell
# Last Updated: 2024-03-26

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# REMEMBER TO INCREASE THE ROW LOOP BY 1 WHEN YOU ADD A NEW TASK

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Creates a json file for my Technical Task Log Using a Excel Sheet

import json
import pandas as pd

# Define variable to load the Excel Work book
TechSheet = pd.read_excel('TaskSheet.xlsx', dtype='string')
# Number of Full rows
fullrows = 2
  
# Iterate the loop to read the cell values within the TimeSheet
FirstRow = True
HeaderList = []
jsonList = []

# Create a List of the Column Header
for col in TechSheet:
    HeaderList.append(col)

# Loop thu each row given the number of full row
# range(#) set to number of Logs
for row in range(4):
    TaskJson = {}
    for col in TechSheet:
        if col == HeaderList[3]:
            TaskJson[col] = TechSheet[col][row][:-9]
        else:
            TaskJson[col] = TechSheet[col][row]
    jsonList.append(TaskJson)

# print(HeaderList)
print(jsonList)

# Writing JSON data to a file
with open("TaskSheet.json", "w") as json_file:
    json.dump(jsonList,json_file,indent=4)