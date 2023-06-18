name='aadhya'

if name == 'rishi':
    print('hi Rishi') #blank space is intendation
    #This is a block or a clause,a block is made of line of code that is intended at same level
    #block increases with intendation increases and ends when it returns to previous level
    #a new block also begins after :
    #blank lines are ignored
print('done') 

password = 'fish'
if password == 'fish':
    print('access granted')
else:
    print('wrong password')

name = 'bob'
age= 3000
if name =='alice':
    print('hi alice')
elif age <12:
    print('youre not alice')

elif age >2000:
    print('youre the one!')

elif age>100:
    print('youre not alice granny')

else :
    print('we cant find anyone :(')



#weird condition, truthy and falsy values

print('whats your name')
name =input() #the input will take an input but give us a string valu
if name: #here name will search of boolean true or false,but as there was a value given in form of string,this will work # truthly value
    print('thanks for entering a name')

else:
    print ("you did not enter a name") # this will be executed if we do not input anything

    #values 0, 0.0 are considered falsy values along with empty strings
    #when used with conditions,they are considered false values
