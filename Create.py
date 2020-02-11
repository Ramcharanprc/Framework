import Miscellaneous as MSC
def create():
	fieldValues = []
	for index in range(0, len(MSC.fieldNames) - 1):
		userInput = input("Enter " + MSC.fieldNames[index] +": ")
		if(index == 0):
			fieldValues.append(int(userInput))
		else:	
			fieldValues.append(userInput)
	fieldValues.append(MSC.active)
	fieldValueTuple = tuple(fieldValues)
	insertQuery = "insert into " + (MSC.tableName) + " values" + str(fieldValueTuple)
	MSC.connection.execute(insertQuery)
	MSC.connection.commit()
	print(MSC.getGeneralMessage("Create") + '\n')
	
