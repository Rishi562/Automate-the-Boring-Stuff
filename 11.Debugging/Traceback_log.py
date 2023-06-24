"""def spam():
    bacon()

def bacon():
    raise Exception('This is the error message.')

spam()
"""


#instead of crashing your program right when an exception occurs, you can write the traceback information to a text file and keep your program running
#we can then look at the text later

import traceback
try:
    raise Exception('This is the error message.')
except:
    errorFile = open('errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
print('The traceback info was written to errorInfo.txt.')
