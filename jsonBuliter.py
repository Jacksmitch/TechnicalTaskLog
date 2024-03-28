# json builder
# Created By Jackson Mitchell
# Last Updated: 2024-03-27
# Creates a json file for a csv with first line of the 
# csv are the keys and the subsequent rows are the corresponding values.
# With each row being an object (excluding the first row)

# For use change the csv and json names to your desired csv and json files

import json, csv

# Iterate the loop to read the cell values within the TimeSheet
# Loop thu each row given the number of full row
# range(#) set to number of Logs
with open('TaskSheet.csv', newline='') as TaskSheet:

    reader = csv.reader(TaskSheet, delimiter=',')

    jsonList = []
    # Loop thru rows then columns of the csv not including the first row
    for i,row in enumerate(reader):
        # print(i,row)
        # Create a List of the Column Header
        if i == 0:
            HeaderList = row
        else:
            TaskJson = {}
            for ci,col in enumerate(row):
                TaskJson[HeaderList[ci]] = col
            jsonList.append(TaskJson)

print(jsonList)
# Writing JSON data to a file
with open("TaskSheet.json", "w") as json_file:
    json.dump(jsonList,json_file,indent=4)