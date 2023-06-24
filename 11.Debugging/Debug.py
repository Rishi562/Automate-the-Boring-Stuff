#find the root cause of bugs in program fast
import traceback

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')
    
    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)

#print(boxPrint('*' , 15, 5))

#if we do the below- 

print(boxPrint('*' , 15, 5)) #does not run as we want#bug

#this whole error message will be called a traceback




