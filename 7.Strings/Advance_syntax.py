#strings can begin and end with double quotes or single quote or 
#we can also use escape characters i\when using ''

#name = 'this is Rishi\'s laptop ' #for single quote
#name = 'this is Rishi\"s laptop ' #for double quote
name = 'this is Rishi\t laptop '  #for tab
print('this is Rishi\n laptop ' ) #for new line 
print('this is Rishi\\ laptop ' ) #backslash single\
print(name)

# RAW String
#begins with a r before it

print(r'this is Rishi\'s laptop') # here backslash will be part of the print

#multiline string
# ''' '''   or """" """"   #gives us flexiblity or multiline
print("""It was a dark and stormy night,
and the skipper said to the mate : 
Mate, tell me a story.
And this is the story he told:
""")

spam = """It was a dark and stormy night,
and the skipper said to the mate : 
Mate, tell me a story.
And this is the story he told:
"""

print(len(spam ))





