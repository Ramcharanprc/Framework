def create():
	fieldValues = []
	for index in range(0, len(fieldNames) - 1):
		userInput = input("Enter " + fieldNames[index] +": ")
		if(index == 0):
			fieldValues.append(int(userInput))
		else:	
			fieldValues.append(userInput)
	fieldValues.append(active)
	fieldValueTuple = tuple(fieldValues)
	insertQuery = "insert into " + (tableName) + " values" + str(fieldValueTuple)
	connection.execute(insertQuery)
	connection.commit()
	print(printGeneralMessage("Create"))
