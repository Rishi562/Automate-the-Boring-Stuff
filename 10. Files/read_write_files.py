# 3 steps to reading and writing files to python
# call the open function open (), pass it a file name like open(password.txt)
#opens the file in read mode

hellofile = open(r'C:\Users\rishi\OneDrive\Desktop\doc.txt') #opens in write mode with w
content = hellofile.read()

print(content)
hellofile.close() #closes the file


#shelve module - used to store list and dict in binary file
import shelve




