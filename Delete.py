# Delete module.
def delete():
	matchedRecord = getRecord()
	printRecord(matchedRecord)
	userConfirmation = input(getGeneralMessage("Delete_Prompt"))
	if(userConfirmation == 'y'):
		query = connection.execute("update " + tableName + " set " + columnNames[-1] + " = '" + inactive + "' where " + columnNames[0] + " = '" + matchedRecord[0] + "'")
		connection.commit()
	print(getGeneralMessage("Delete"))
