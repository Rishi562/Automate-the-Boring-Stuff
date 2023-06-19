#methods are functions that are called on values
#list methods example - index append insert remove sort 

spam = [10,20,30,40,50,60]
print(spam.index(10)) # gives 0


spam = [10,20,30,40,50,60, 10,20,50]
print(spam.index(50)) # gives the first value it sees


spam.append(90) # adds a value to end of the list
print(spam)

spam.insert(1, 33) #inserts 33 at index 1
print(spam)

# we dont assign while calling methods lioke spam = spam.append(40). a method itself has none value to it

spam.remove(50)  #removes the first value found
print(spam)

del spam [0] # del method removes from index
print(spam)

spam.sort() #rearranges in order
print(spam)


eggs =['ants','cats','bees','sdf','asfsa']
eggs.sort()
print(eggs) 



eggs =['ants','cats','bees','sdf','asfsa','ants','Cats','Bees','sdf','Asfsa']
eggs.sort(reverse = True) #sorts in reverse order
print(eggs) 

eggs =['ants','Cats','Bees','sdf','Asfsa']
eggs.sort() #pushes the lowercase to last even if it is a
print(eggs)

eggs =['ants','cats','bees','sdf','asfsa','ants','Cats','Bees','sdf','Asfsa']
eggs.sort(key =str.lower) #sorts according to alphabets
print(eggs) 



