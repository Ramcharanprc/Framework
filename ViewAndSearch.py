# View and search functions.
import Miscellaneous as MSC
def view():
	recordCount = MSC.connection.execute("select count(*) from " + MSC.tableName + " where " + MSC.columnNames[-1] + " = '" + MSC.active + "'")
	cursor = MSC.connection.execute("select * from " + MSC.tableName + " where " + MSC.columnNames[-1] + " = '" + MSC.active + "'")
	for count in recordCount:
		if (count[0] != 0):
			for row in cursor:
				MSC.printRecord(row)
			print(MSC.getGeneralMessage('Print') + '\n')
		else:
			print('No Records are found.\nPlease create new records.\n')

def search():
	MSC.printRecord(MSC.getRecord()) # returned record from getRecord() is passed as an argument to printRecord()
	if(MSC.flag != 0):
		print(MSC.getGeneralMessage("Search") + '\n')
	else:
		print(MSC.getGeneralMessage('Error'))
		print()