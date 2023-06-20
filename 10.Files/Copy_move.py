# organize the prexisting file on HDD
#shutil #shell utility


import shutil
#shutil.copy(r'C:\Users\rishi\OneDrive\Desktop\doc.txt', r'C:\Users\rishi\OneDrive\Desktop\DevOps') #copies the file to devops folder
#shutil.copy(r'C:\Users\rishi\OneDrive\Desktop\doc.txt', r'C:\Users\rishi\OneDrive\Desktop\DevOps\copiedfile.txt') #copy and rename at same time

#shutil.copytree(r'C:\Users\rishi\OneDrive\Desktop\Folder1', r'C:\Users\rishi\OneDrive\Desktop\backup') #copies the folder as another name

#shutil.move(r'C:\Users\rishi\OneDrive\Desktop\backup\doc.txt' , r'C:\Users\rishi\OneDrive\Desktop\Folder1\Walnut') #moves the file from here to another folder

shutil.move(r'C:\Users\rishi\OneDrive\Desktop\backup\doc.txt' , r'C:\Users\rishi\OneDrive\Desktop\backup\Walnut.txt') #used to rename file,move the file in same folder



