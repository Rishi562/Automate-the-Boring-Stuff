#a string method returns a new string unlike lists which modifies the same in place as strings are immutable

#upper(), lower() , title()

spam='hello worlldddddddddddddddddd'

print(spam.upper())
print(spam.lower())

#but if we do
spam = spam.upper()
print(spam) #the new string in spam is now all upper


#isupper(), islower() these return boolean value

spam='hello worlldddddddddddddddddd'
print(spam.isupper()) #returns false

#we can aslo do it this way directly to string
egg = 'hello'.upper()
print(egg) #returns HELLO

#More Methods
#isalpha()  #returns True if letters only
#isalnum()  #returns True if has letters and numbers
#isdecimal()#returns True if has numbers only
#isspace()  #returns True if it has only whitespace ,include index to point at whitespace #egg[5] 5 is the middle space between hello and world
#istitle()  #returns True if first letter of all words are upper




