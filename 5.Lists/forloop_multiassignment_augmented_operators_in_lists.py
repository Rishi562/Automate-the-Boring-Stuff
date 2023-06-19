# RANGE

for i in range(4): #this is same as [0,1,2,3]
    print(i)


for i in [0,1,2,3] :
    print(i)

#both above are same



x=list(range(4))
print(x)

x=list(range(0,100,2)) #range is from 0 to 100 and step is twice
print(x)

supplies = ['pens', 'staple','binders','flame throwers']
for i in range(len(supplies)) :
    print('index ' + str(i) + ' in supplies is: ' + supplies[i])

#here we can use for loop cariable i to print the index as well as the list value
#very handy


#Multiple Assignemnt

cat = ['fat','orange','loud']

size,color,disposition = cat # size is fat now
print(size)

#2nd assignment method
size,color,disposition = 'skinny','black','quiet'
print(color)



#Augmented Assignemnt Operators

egg = 42
egg = egg +1 
egg += 1 #same thing as above
print (egg)
