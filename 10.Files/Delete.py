import os
import shutil
#print(os.getcwd())

#os.unlink(filename) #this will delete file in the same directory we are in
#os.rmdir(foldername) #deletes the folder,folder needs to be completely empty

#shutil.rmtree(r'c:\Users\rishi\\doc.txt') #deletes the folder with content

#deletes permanently,does not send to recyclebin

#refer video for dry run
#these are dangerous as they are deleting it permanently

#We install 3rd party module #send2trash

import send2trash
#send2trash.send2trash(r'c:\Users\rishi\\doc.txt')
#this will delete file and send to recyclebin

