# List is a value that contains value (items)
# it contains multiple values in an ordered sequence
# values inside a list are sometimes called items
# a list begins and ends with [], values inside this are separated with commas

spam = ['cat', 'bat', 'rat','mat'] # can be assigned to a variable like any other value

print(spam[1] , spam[0]) # we can access the items inside the list by [index number]


# List of Lists
# A list can also contain other list values, these can be accessed using multiple indexes

spam = [['cat','bat'], [10,20,30,40,50]]

print(spam[0]) #here index 0 will return both cat and bat

print(spam[0][1]) # here it will only return cat

print(spam[1]) # returns 10,20,30....
print(spam[1][4]) # prints 50

print(spam[-1][-1]) #returns 50
print('the ' + spam[-2][-2] + ' is afraid of the number ' + str(spam[-1][-3])) # returns cat with 50, here we convert int to string to print with +


# SLICES
# a slice can get several values from the list as opposed to index which gets a single value
# it returns a list
spam = [10,20,30,40,50]
print(spam[2:4]) #only gives 30,40


#changing a list's item
spam=[10,20,30]
spam[1]='hello'
print(spam) # 20 is replaced

spam[0:3] = ['cat','dog','mat'] #replaces 10,20,30
print(spam) 
print(spam[:2]) #shortcut
print(spam[1:])

#delete value from string
spam=[10,20,30,40,50,60,70]
del spam[2:4]
print(spam)

print(len(spam))

egg = [10,20,30] + [40,50,60] #list concat just like string
print(egg)

# we can do most things with list just like strings

egg= [10,20,30] * 3
print(egg)

ham= 'hello'
print(list(ham)) # list function returns it in list form

#in and not in

x = 10 in egg  # evaluates to true
print(x)

x = 10 not in egg # evaluates to False
print(x)