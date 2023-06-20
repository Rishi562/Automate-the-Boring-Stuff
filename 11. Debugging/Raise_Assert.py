# An assertion is a sanity check to make sure your code isn’t doing something obviously wrong
#We should not handle assert statements with try and except; if an assert fails, your program should crash

#Using an Assertion in a Traffic Light Simulation


market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}

def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'

print(market_2nd)
switchLights(market_2nd)
print(market_2nd)

# assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)