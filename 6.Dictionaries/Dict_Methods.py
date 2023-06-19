# methods which return list like values for dic

#keys() ,  values() , items()

eggs = {'name' : 'rishi', 'age' : 25 , 'species':'human'}

ham = {'age' : 25 , 'species':'human','name' : 'rishi'}


print(list(eggs.keys()))
print(list(eggs.values()))
print(list(eggs.items()))

for k in eggs.keys():
    print(k)

for v in eggs.values():
    print(v)

for k,v in eggs.items(): #items give us 2 values , key and pair
    print(k,v)

#GET Method

print (eggs.get('age',0)) #gives us 23

#if there was no age or value for age,it would give us 0



