# We can use  module openpyxl ()
#this can also work with libra and open office

import openpyxl
import os


os.chdir('C:\\Users\\rishi\\OneDrive\\Desktop\\backup') 
print('the directory hsa been changed to') #changes directory
print (os.getcwd())

#create a workbook object

workbook = openpyxl.load_workbook('rent furn.xlsx')
type(workbook) #defines it is a workbook object


#if we wan a sheet we can call it by Name
workbook.get_sheet_names() #print to return their name

sheet['A1'] 
cell = sheet['A1']
print(cell.value  )




