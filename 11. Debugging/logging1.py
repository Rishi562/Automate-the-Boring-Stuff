import logging
logging.basicConfig(filename = 'mylogs.txt',level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')  #we created a logging file also here
logging.disable(logging.CRITICAL) #disables the logs

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s%%)'  % (n))
    total = 1
    for i in range(1,n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)'  % (n))
    return total

print(factorial(5))
logging.debug('End of program')


#There are 5 types of log level fom lowest to highest
#debug,info , warning,error,critical

#we can write all these to a text file