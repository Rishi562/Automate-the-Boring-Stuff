spam = 0
while  spam <5:   #here if we use if,it will only print once
    #if ends when condition is true,while while goes back till all conditions are true
    print('hello')
    spam=spam+1
    

#break and continue
mont = 0
while mont < 5:
    mont = mont+1
    if mont == 3:
        continue
    print ('mont is ' + str(mont))