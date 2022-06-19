import numpy as np
state = [['blank', 'X', 'blank'],
         ['blank', 'O', 'X'],
         ['O', 'X', 'blank']] #initial board

def ai_player(s):
    count_X = sum([i.count('X') for i in s])
    count_O = sum([i.count('O') for i in s])

    if count_X - count_O == 1:
        return 'O'

    elif count_O - count_X == 1:
        return 'X'

    else:
        return 'X'

def actions(s):
    p = set(zip(*np.argwhere(s == 'blank')))
    return p

#print(player(state))
print(actions(state))
