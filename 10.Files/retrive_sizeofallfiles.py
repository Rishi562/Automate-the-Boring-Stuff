import os

totalsize = 0 
for filename in os.listdir(r'C:\Users\rishi\OneDrive\Desktop'):
    if not os.path.isfile(os.path.join (r'C:\Users\rishi\OneDrive\Desktop', filename)) :
        continue
    totalsize = totalsize + os.path.getsize(os.path.join (r'C:\Users\rishi\OneDrive\Desktop', filename))

print(totalsize)