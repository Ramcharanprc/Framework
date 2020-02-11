import Miscellaneous as MSC
def update():
	MSC.printRecord(MSC.getRecord())
	for updateCounter in range(1, len(MSC.fieldNames) - 1):
		print(str(updateCounter) + ". " + MSC.fieldNames[updateCounter])
	userOption = int(input(MSC.getGeneralMessage('Update_Prompt')))
	MSC.connection.execute("update " + MSC.tableName + " set " + MSC.columnNames[userOption] + " = '" + input("Enter " + MSC.fieldNames[userOption] + ": ") + "' where " + MSC.columnNames[0] + " = '" + MSC.userInput + "';")
	MSC.connection.commit()
	print(MSC.getGeneralMessage('Update'))

