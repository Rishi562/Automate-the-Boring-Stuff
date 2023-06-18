#variables inside the function can have the same name as variable outside the function
#they are considered 2 seperate variables

spam =42 #global variable

def eggs():
    spam = 42 #local variable is created when a function is called and then destroyed when function is returned

#global scope is created when program starts and the program stops

#1. Local Variables cannot be used in the global scope
def spam():
    eggs=9
spam()
print(eggs) # 9 will not be printed as it was destroyed when spam was called
    
    
#2. local scope cannot use variables in other functions local scope

def spam():
    eggs=9
    bacon()
    print(eggs)

def bacon ():
    ham=101
    eggs=0
spam()

#3. Global variables can be accessed from a local scope

def spam():
    print(eggs)
    
eggs=42
spam()

#4. Assign a new value to a global variable from inside of a function

def spam():
    global eggs  #eggs will always refer to the global variable which is 42
    eggs = 'hello'
    print(eggs)

eggs = 42
spam()
print(eggs)