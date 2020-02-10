# Framework with CRUD functions.
import sqlite3
import

databaseName = 'Framework.db'
generalTable = 'generalConfigTable'
menuFile = 'menu.cfg'
connection = sqlite3.connect(databaseName)
generalConfigurations = connection.execute("select * from " + generalTable)
general = {}
for row in generalConfigurations:
	general[row[0]] = row[1]

def getConfigurationMessage(configurationKey):
	return general[configurationKey]
tableName = getConfigurationMessage('Table_Name')

fieldTable = connection.execute('.pragma table_info ' + general)
fieldNames = []
columnNames = []
for row in fieldTable:
	columnNames.append(row[1])
	fieldWithoutSpace = row[1].replace("_", " ")
	filedNames.append(fieldWithoutSpace)

def printRecord(record):
	for index in range(0, len(fieldNames) - 1):
		print(fieldNames[index] +": "+ (record[index]))
		print()

