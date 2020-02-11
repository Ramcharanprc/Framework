# Framework with CRUD functions.
import sqlite3
import Create
import ViewAndSearch
import UpdateModule
import Delete
import Exit

active = 'A'
inactive = 'I'
databaseName = 'Framework.db'
generalTable = 'GeneralConfigTable'
menuFile = 'Menu.cfg'
connection = sqlite3.connect(databaseName)
generalConfigurations = connection.execute("select * from " + generalTable)
general = {}
for row in generalConfigurations:
	general[row[0]] = row[1]

def getGeneralMessage(configurationKey):
	return general[configurationKey]
tableName = getGeneralMessage('Table_Name')

fieldTable = connection.execute('.pragma table_info ' + tableName)
fieldNames = []
columnNames = []
for row in fieldTable:
	columnNames.append(row[1])
	fieldWithSpace = row[1].replace("_", " ")
	fieldNames.append(fieldWithSpace)
menu = []
with open(menuFile, 'r') as fpFile:
	for line in fpFile:
		menu.append(line)

def printRecord(record):
	for index in range(0, len(fieldNames) - 1):
		print(fieldNames[index] +": "+ (record[index]))
		print()

def getRecord():
	global userInput
	userInput = input('Enter ' + fieldNames[0] + ': ')
	data = connection.execute('select * from ' + tableName + ' where ' + columnNames[0] + ' = "' + userInput + '" and ' + columnNames[-1] ' = "' + active + '"')
	for record in data:
		if(len(record) != 0):
			return record
		else:
			print(getGeneralMessage('Error'))
			showMenu()

def showMenu():
	for line in menu:
		print(line)
	userChoice = int(input('Enter your choice: '))
	if(userChoice > 0 and userChoice < 7):
		[create, view, update, delete, search, Exit][userChoice - 1]()
	else:
		print('Invalid option!\nPlease enter a valid option.')
	showMenu()
showmenu()
