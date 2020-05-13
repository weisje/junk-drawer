###############################################################################
# Import Name: JunkDrawer.py
# Version: 0.1
# First Development Date: 13 May 2020 (13/05/2020)
# Latest Development Date: 13 May 2020 (13/05/2020)
# Program Name: Python Function Junk Drawer
# Developer: John Weis
# Purpose: This program is a library of commonly used Python functions so I don't have to keep typing them
###############################################################################

#*IMPORT BLOCK BEGIN*

#import datetime
import os
import sys
import time

#*IMPORT BLOCK END*

#*GLOBAL VARIABLE BLOCK BEGIN*

latestDevelopmentDate = '13 May 2020 (13/05/2020)'
#*GLOBAL VARIABLE BLOCK END*

#*LAMBDA BLOCK BEGIN*

sleep = lambda seconds = 2: time.sleep(seconds)

#*LAMBDA BLOCK END*

#*FUNCTION BLOCK BEGIN*(13/05/2020-JW)

## Function Description
# def foo():
#
#	#**VARIABLE BLOCK BEGIN**

#	#**VARIABLE BLOCK END**
#
#	pass

# Displays information about the program when about() is called.  Prints information to console.
def about():
	#**VARIABLE BLOCK BEGIN**
	importName = 'JunkDrawer.py'
	versionNum = 0.1
	firstDevelopmentDate = '13 May 2020 (13/05/2020)'
	latestDevelopmentDate = latestDevelopmentDate
	programName = 'Python Function Junk Drawer'
	Developer =  'John Weis'
	#**VARIABLE BLOCK END**

	print("\nProgram Name: %s\nVersion Number: %.1f" % (programName, versionNum))
	print("latestDevelopmentDate: %s" % (latestDevelopmentDate))
	print("Developer: %s" % developerName)
	sleep(2)

# Function Description
def clear():
	#**VARIABLE BLOCK BEGIN**
	sendCommand = 'clear'
	#**VARIABLE BLOCK END**
	if sys.platform == 'win32':
		sendCommand = 'cls'

	try:
		os.system(sendCommand)
	except Exception as exception:
		print(exception)



###############################################################################
# Notes: 
# (13/05/2020-JW): Created main file for future development
###############################################################################
