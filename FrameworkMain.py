# Framework with CRUD functions.
import sqlite3

databaseName = 'Framework.db'
generalTable = 'generalConfigTable'
connection = sqlite3.connect(databaseName)
generalConfigurations = connection.execute("select * from ")
fieldTable = connection.execute('.pragma table_info ' + general)
fieldNames = []
for row in fieldTable:
	
