# View and search functions.
import Miscellaneous as MSC
def view():
	cursor = MSC.connection.execute("select * from " + tableName)
	for row in cursor:
		MSC.printRecord(row)
	print(MSC.getGeneralMessage("Print"))

def search():
	MSC.printRecord(MSC.getRecord()) # returned record from getRecord() is passed as an argument to printRecord()
	print(MSC.getGeneralMessage("Search"))