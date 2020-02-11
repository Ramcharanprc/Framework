import Miscellaneous as MSC
def update():
	MSC.printRecord(MSC.getRecord())
	if(MSC.flag != 0):
		for updateCounter in range(1, len(MSC.fieldNames) - 1):
			print(str(updateCounter) + ". " + MSC.fieldNames[updateCounter])
		while True:
			try:
				userOption = int(input(MSC.getGeneralMessage('Update_Prompt')))
				MSC.connection.execute("update " + MSC.tableName + " set " + MSC.columnNames[userOption] + " = '" + input("Enter " + MSC.fieldNames[userOption] + ": ") + "' where " + MSC.columnNames[0] + " = '" + MSC.userInput + "';")
				MSC.connection.commit()
				print(MSC.getGeneralMessage('Update') + '\n')
				break
			except IndexError:
				print('Invalid option.\n')
	else:
		print(MSC.getGeneralMessage('Error'))
		print()