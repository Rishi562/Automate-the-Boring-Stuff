# request module lets us download easily without having to worry about complicated issues like network errors, connection problem or data compression
#3rd party module

import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.status_code

#the get function returns a response object,store it in avariable
#this is the response that the webserver gave us for our request
#200 status code means it was executed

#the downloaded webpage is stored as a string in the response object text variable res.text

print (len(res.text))

#print (res.text[0:500])


print (res.raise_for_status()) #no response
#simpler way to check for success

#badres = requests.get('https://automatetheboringstuff.com/files/sdfjksdhfudsu')
#print (badres.raise_for_status()) # we can also wrap this in a try and except without crashing 

#now saving the file
#first open the file in write binary mode:passign wb as 2nd argument
#this is to maintain the encoding

playFile = open('romeojuliet.txt','wb')

for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()





