# Search module framework.
import sqlite3
menuFile = "Menu.cfg"
generalTable = "GeneralConfigTable"
fieldNames = []
record = []
active = "A"
inactive = "I"
tableName = "Employee"
connection = sqlite3.connect("Framework.db")
tableInfo = connection.execute("pragma table_info('" + tableName + "')")
for column in tableInfo:
	fieldNames.append(column[1])
# print(fieldNames[0])
# def getRecord():
# 	userInput = input("Enter " + fieldNames[0] + ": ")
# 	cursor = connection.execute("select * from "+ tableName + " where " + fieldNames[0] + " = " + userInput + " and " + fieldNames[-1] + " = '" + active + "'")
# 	# printRecord(cursor)
# 	for value in cursor:
# 		for counter in range(0, len(fieldNames) - 1):
# 			record.append(value[counter])
# 	# print(record)
# 	return record
def printRecord(record):
	for index in range(0, len(fieldNames) -1):
		print(fieldNames[index] + " : " + record[index])

printRecord()

def view():
	cursor = connection.execute("select * from " + tableName)
	for row in cursor:
		printRecord(row)
	print(getGeneralMessage("Print"))
# view()

def search():
	printRecord(getRecord())
	print(getGeneralMessage("Search"))
# search()