# list and strings are similar

# we can perform almost all operations

#a list is a mutable whereas a string is immuatable ,it cannot be changed

print(list('hello')) 
name = 'Rishi'

print(name[0]) # gives index1 value

print(name[0:3])

x = 'ish' in name
print(x) # gives true

########################################3

# we cannot add/modify values to strings, there is a proper way to do it

#we need to create a new string from slices

name = 'Rishi the Raj'
newname = name[0:7] + 'the ' + name[8:12]
print(newname) 


#we are copting the value from old to new
#above one is complicated

 

 #lists use references #imp
#REFERENCES

spam=42
cheese=spam
spam=100
print(spam)  #this now prints 100 

#but

spam = [0,1,2,3,4,5]
cheese=spam
cheese[1] = 'hello'
print(cheese) # here index 1 will be changed to hello
print(spam)# here also spam will change index to 1 because they use the same reference to point to the list

#as list is mutable it can change
#immutable values do not have this issue







