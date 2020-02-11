# View and search functions.
import FrameworkMain
def view():
	cursor = connection.execute("select * from " + tableName)
	for row in cursor:
		printRecord(row)
	print(getGeneralMessage("Print"))

def search():
	printRecord(getRecord()) # returned record from getRecord() is passed as an argument to printRecord()
	print(getGeneralMessage("Search"))