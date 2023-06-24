#walk through the folder tree and do operations like rename or copy

#os.walk()

import os

for foldername, subfolders, filename in os.walk(r'C:\Users\rishi\OneDrive\Desktop\backup'):
    print('The folder is ' + foldername )
    print('The subfolder in ' + foldername + ' are: ' + str(subfolders))
    print('The filenames in ' + foldername + ' are: ' + str(filename))
    print()

#review this again for further actions to do
