# Dictionaries is a collection of many values
# indexes in dictionary can use different datatype not just integers
#indexes in dict is called key , and the associated value is called a key value pair

myCat = {'size' : 'fat', 'color' : 'green', 'disposition' : 'loud'}

# dictionary are represented by {}
#size and fat are key value pair here
#here keys are the sirings size,color and dispo
#here values are fat green and loud
#variables hold references to the dict,not the dict itself

print(myCat['size'])

#we can aslo use int in dict keys

myfat = {12345:'luggage key', 42:'answer'}
print(myfat[12345])

#Values inside a Dict are unordered unlike list

eggs = {'name' : 'rishi', 'age' : 25 , 'species':'human'}

ham = {'age' : 25 , 'species':'human','name' : 'rishi'}
print(eggs==ham) # answer is true even when the order of the values inside is not same

#if a key does not exist,it gives a keyerror

print('name' in eggs)  # gives true, we can check if a key exists in a dict or not

print('name' not in eggs)

