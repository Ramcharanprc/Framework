# Framework with CRUD functions.

import Create
import ViewAndSearch
import UpdateModule
import Delete
import Exit

menuFile = 'Menu.cfg'
menu = []
with open(menuFile, 'r') as fpFile:
	for lineWithoutSpace in fpFile:
		lineWithSpace = lineWithoutSpace.replace('\n', '')
		menu.append(lineWithSpace)

def showMenu():
	for line in menu:
		print(line)
	userChoice = int(input('Enter your choice: '))
	if(userChoice > 0 and userChoice < 7):
		[Create.create, ViewAndSearch.view, UpdateModule.update, Delete.delete, ViewAndSearch.search, Exit.Exit][userChoice - 1]()
	else:
		print('Invalid option!\nPlease enter a valid option.\n')
	showMenu()
showMenu()
