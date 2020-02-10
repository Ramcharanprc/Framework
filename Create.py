import sqlite3
Zero = 0
activeStatus = "A"
inactiveStatus = "D"
database = "Sindhu.db"
menuFile = "Menu.cfg"
generalTable = "General"
menuList = []
fieldList = []
connection = sqlite3.connect(database)

def create():
	print(fieldList)
	fieldValues = []
	for index in range(Zero, len(fieldList) - 1):
		userInput = input("Enter " + fieldList[index] +": ")
		if(index == Zero):
			fieldValues.append(int(userInput))
		else:	
			fieldValues.append(userInput)
	fieldValues.append(activeStatus)		
	fieldValueTuple = tuple(fieldValues)
	insertQuery = "insert into " + (tableName) + " values" + str(fieldValueTuple)
	connection.execute(insertQuery)
	connection.commit()
	print(getGeneralMessage("Create"))
