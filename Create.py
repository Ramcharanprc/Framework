import sqlite3
active = "A"
inactive = "D"
database = "FrameWork.db"
menuFile = "Menu.cfg"
generalTable = "General"
menuList = []
fieldList = []
connection = sqlite3.connect(database)

def create():
	fieldValues = []
	for index in range(Zero, len(fieldList) - 1):
		userInput = input("Enter " + fieldList[index] +": ")
		if(index == 0):
			fieldValues.append(int(userInput))
		else:	
			fieldValues.append(userInput)
	fieldValues.append(activeStatus)		
	fieldValueTuple = tuple(fieldValues)
	insertQuery = "insert into " + (tableName) + " values" + str(fieldValueTuple)
	connection.execute(insertQuery)
	connection.commit()
	printGeneralMessage("Create")
