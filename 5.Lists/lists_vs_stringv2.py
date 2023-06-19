#mutable - list,set,dictionary
#immutable-string,tuple,int

def eggs(someParameter):
    someParameter.append('hello')

spam=[1,2,3]
eggs(spam)

print (spam) #changes made inside the eggs function are reflected outside into spam

#copy Module
import copy #makes a copy of the original list

spam = ['a','b','c','d']
cheese = copy.deepcopy(spam)

cheese[1] = 42 

print(cheese)  
print(spam)   #now cheese is not replaced by index1 42


#lists can pan multiple line of code

spam = ['hello'
        ,'world',
        'fu']      #considers a single line of code
print(spam)
