#datastructures are list of dictionaries

theboard = {'top-l':' ','top-m':' ','top-r':' ',
            'mid-l':' ','mid-m':' ','mid-r':' ',
            'low-l':' ','low-m':' ','low-r':' '}

import pprint
pprint.pprint(theboard)

#theboard['mid-m'] = 'X'
#pprint.pprint(theboard)

def printBoard(board):
    print(board['top-l'] + '|' + board['top-m'] + '|' + board['top-r'])
    print('-----')
    print(board['mid-l'] + '|' + board['mid-m'] + '|' + board['mid-r'])
    print('-----')
    print(board['low-l'] + '|' + board['low-m'] + '|' + board['low-r'])

printBoard(theboard)

# print(type(theboard))
