import sqlite3
import FrameworkMain as FW

active = 'A'
inactive = 'I'
databaseName = 'Framework.db'
generalTable = 'GeneralConfigTable'
connection = sqlite3.connect(databaseName)
generalConfigurations = connection.execute("select * from " + generalTable)
general = {}
for row in generalConfigurations:
	general[row[0]] = row[1]

def getGeneralMessage(configurationKey):
	return general[configurationKey]
tableName = getGeneralMessage('Table_Name')

fieldTable = connection.execute('pragma table_info(' + tableName + ')')
fieldNames = []
columnNames = []
for row in fieldTable:
	columnNames.append(row[1])
	fieldWithSpace = row[1].replace("_", " ")
	fieldNames.append(fieldWithSpace)


def printRecord(record):
	for index in range(0, len(fieldNames) - 1):
		print(fieldNames[index] +": "+ (record[index]))
		print()

def getRecord():
	global userInput
	userInput = input('Enter ' + fieldNames[0] + ': ')
	query = 'select * from ' + tableName + ' where ' + columnNames[0] + ' = "' + userInput + '" and ' + columnNames[-1] ' = "' + active + '"'
	print(query)
	data = connection.execute(query)
	for record in data:
		if(len(record) != 0):
			return record
		else:
			print(getGeneralMessage('Error'))
			FW.showMenu()
