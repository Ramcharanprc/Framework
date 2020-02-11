# Delete module.
import Miscellaneous as MSC
def delete():
	matchedRecord = MSC.getRecord()
	MSC.printRecord(matchedRecord)
	if(MSC.flag != 0):
		userConfirmation = input(MSC.getGeneralMessage("Delete_Prompt"))
		if(userConfirmation == 'y'):
			query = MSC.connection.execute("update " + MSC.tableName + " set " + MSC.columnNames[-1] + " = '" + MSC.inactive + "' where " + MSC.columnNames[0] + " = '" + matchedRecord[0] + "'")
			MSC.connection.commit()
			print(MSC.getGeneralMessage("Delete"))
	else:
		print(MSC.getGeneralMessage('Error'))
		print()