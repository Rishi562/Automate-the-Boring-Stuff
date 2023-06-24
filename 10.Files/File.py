# Files and Folders and how Python can work with them
# a file has 2 key properties- file name and file path(directory)

import os #os modules contains different file path related modules

#os.getcwd()  #current cirectory
#os.chdir() #change dir

#absolute path begin with root folder like c:\
#relative path will be like \users\file.txt

#print(os.path.abspath('IMG_8520.jpg'))

print(os.path.dirname(r'C:\Users\rishi\OneDrive\Desktop\IMG_8520.jpg'))
#gives us the directory name
print(os.path.basename(r'C:\Users\rishi\OneDrive\Desktop\IMG_8520.jpg'))
#gives us the name of the file or the last folder

print(os.path.exists(r'C:\Users\rishi\OneDrive\Desktop\IMG_8520.jpg'))
#returns true if the file path exists
print(os.path.isfile(r'C:\Users\rishi\OneDrive\Desktop\IMG_8520.jpg'))
#returns true if the file  exists
print(os.path.isdir(r'C:\Users\rishi\OneDrive\Desktop'))
#returns true if the dir path exists #remove img to get true

print(os.path.getsize(r'C:\Users\rishi\OneDrive\Desktop\IMG_8520.jpg'))
#gives size of file
print(os.listdir(r'C:\Users\rishi\OneDrive\Desktop'))
#gives us the all the files present in the desktop folder