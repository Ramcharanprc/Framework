def update():
	readUserInput()
	printRecord(getRecord())
	for updateCounter in range(1, len(fieldNames)):
		print(str(updateCounter) + ". " + fieldNames[updateCounter])
	userOption = input(generalMessage('Update_prompt'))
	connection.execute("update " + tableName + " set " + columnNames[userOption] +" = '" + input("Enter "+ fieldNames[userOption] + "' where " + columnName[0] +" = '" + userInput + "';")
	connection.commit()
	print(generalMessage('Update'))

