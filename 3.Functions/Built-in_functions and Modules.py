#BUILTIN FUNCTIONS
#builtin functions are basic set of functions provided by python
#examples print(),int(),input(),len()


#MODULES
#Standard library in python
#lots of modules in python standard library
#We need to import the modules to use them like import math at the top
#these contain related functions to be used in the program
# #math module is a spereate file that has a reusable math module codes

# now here math is an object like a string 
# so we can access the methods of this function using the . operator
#import multiple by separating them with a comma

import random,sys,os,math

print(random.randint(0,1000))



#HOW TO TERMINATE A PROGRAM EARLY 
#sometimes we do not want the program to be executed till the bottom of the instructions
#USE sys.exit()

print('hello')
#sys.exit()
print('goodbye')

#THIRD PARTY MODULES
#other that standard library for add on functionality
#can be installed with pip program - should be run from command line
#

import pyperclip

pyperclip.copy('hello world') #copies hello world to clipboard
print(pyperclip.paste()) # pastes what we copied



