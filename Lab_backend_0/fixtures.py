import json
import random as rd

from string import (
    ascii_letters,
    ascii_lowercase,
    ascii_uppercase, digits
)

SYMBOLS = ascii_letters + ascii_lowercase + ascii_uppercase + digits

ATTRIBUTES = [
    'sum_number_in_string',
    'get_leader_string',
    'to_json',
    'get_spiral_number_matrix'
]
SUM_STRING_NUMBER = {
    '0464578809630225': 69,
    '9631465982103241': 64,
    '8708358923336289': 84,
    '7668674612215731': 72,
    '9853966074460144': 76,
    '6156425438133961': 67,
    '9712903108096102': 58,
    '2615124530308719': 57,
    '5987342488194401': 77,
    '8775993294508606': 88,
    '0301961481858622': 64,
    '6584911333123903': 61,
    '3681076003625739': 66,
    '9491677024939004': 74,
    '1099560118912943': 68
}
LEADERS = {
    1: '#\n',
    2: ' #\n'
       '##\n',
    3: '  #\n'
       ' ##\n'
       '###\n',
    4: '   #\n'
       '  ##\n'
       ' ###\n'
       '####\n',
    10: '         #\n'
        '        ##\n'
        '       ###\n'
        '      ####\n'
        '     #####\n'
        '    ######\n'
        '   #######\n'
        '  ########\n'
        ' #########\n'
        '##########\n',
    5: '    #\n'
       '   ##\n'
       '  ###\n'
       ' ####\n'
       '#####\n',
    12: '           #\n'
        '          ##\n'
        '         ###\n'
        '        ####\n'
        '       #####\n'
        '      ######\n'
        '     #######\n'
        '    ########\n'
        '   #########\n'
        '  ##########\n'
        ' ###########\n'
        '############\n'
}

json_datas = {}

for _ in range(5, rd.randint(20, 100)):
    data = {}
    for j in range(1, rd.randint(10, 20)):
        data[''.join(rd.choices(SYMBOLS, k=rd.randint(10, 20)))] = rd.choices(
            SYMBOLS, k=rd.randint(10, 20)
        )
    json_datas[json.dumps(data)] = data

SPIRAL_NUMBERS = {
    1: '1',
    2: '1 2\n4 3',
    3: '1 2 3\n'
       '8 9 4\n'
       '7 6 5',
    4: '1 2 3 4\n'
       '12 13 14 5\n'
       '11 16 15 6\n'
       '10 9 8 7',
    5: '1 2 3 4 5\n'
       '16 17 18 19 6\n'
       '15 24 25 20 7\n'
       '14 23 22 21 8\n'
       '13 12 11 10 9',
    6: '1 2 3 4 5 6\n'
       '20 21 22 23 24 7\n'
       '19 32 33 34 25 8\n'
       '18 31 36 35 26 9\n'
       '17 30 29 28 27 10\n'
       '16 15 14 13 12 11'
}
