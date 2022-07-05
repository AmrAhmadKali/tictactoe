from engine import *

state = [[None, 'X', None],
         [None, 'O', 'X'],
         ['O', 'X', None]] #initial board

###def ai_player(s):
   # count_X = sum([i.count('X') for i in s])
    #count_O = sum([i.count('O') for i in s])

    #if count_X - count_O == 1:
     #   return 'O'

    #elif count_O - count_X == 1:
     #   return 'X'

    #else:
     #   return 'X'

def actions(s):
    p = set()
    for i in range(3):
        for j in range(3):
            if s[i][j] == None:
                possible_move = (i, j)
                p.add(possible_move)
    if p == set():                                                              #   to work on
        print('Full board')
        return 0
    return p

# result function is the get_move() in engine.py

# The winner function is get_winner and is_full() for checking the draw

def terminal(state):
    if get_winner(state) == 'x' or get_winner(state) == 'o' or is_full(state):
        return True
    return False


# If X has won the game, the utility is 1. If O has won the game, the utility is -1. If the game has ended in a tie, the utility is 0.

def utility(state):
    if get_winner(state) == 'x':
        return 1
    elif get_winner(state) == 'o':
        return -1
    else:
        return 0

def minimax(state):




#print(player(state))
print(actions(state))
