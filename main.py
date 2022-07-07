from engine import *
from time import sleep

MIN_PLAYER = 'x'
MAX_PLAYER = 'o'

state = [['o', 'o', 'x'],
         ['x', 'x', 'o'],
         ['o', 'x', 'o']] #initial board

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
            if s[i][j] is None:
                possible_move = (i, j)
                p.add(possible_move)
    if p == set():                                                              #   to work on
        print('Full board')
        return 0
    return p

# result function is the get_move() in engine.py

# The winner function is get_winner and is_full() for checking the draw


def terminal(s):
    winner = get_winner(s)
    if winner == 'x' or winner == 'o' or is_full(s):
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


def play_mode2():
    print('Wellcome to TIC-TAC-TOE AI')
    
    current_board = new_board()
    render(current_board)

    while True:
        if player(current_board) == MAX_PLAYER:
            print(f'Player {player(current_board)} turn')
            sleep(1.5)
            optimal_move = minimax(current_board)
            current_board = make_move(current_board, optimal_move, MAX_PLAYER)
            render(current_board)

            if terminal(current_board):
                break

        elif player(current_board) == MIN_PLAYER:
            print('Your turn')
            opponent_move = get_move()
            if is_valid_move(current_board, opponent_move):
                current_board = make_move(current_board, opponent_move, MIN_PLAYER)
            else:
                print('Invalid move')
                continue

            render(current_board)

            if terminal(current_board):
                break


def max_value(s):
    if terminal(s):
        return utility(s)

    v = -2                  #lowest possible utility
    for action in actions(s):
        v = max(v, min_value(make_move(s, action, MIN_PLAYER)))
    return v


def min_value(s):
    if terminal(s):
        return utility(s)

    v = 3
    for action in actions(s):
        v = min(v, max_value(make_move(s, action, MAX_PLAYER)))
    return v


def minimax(s):
    optimal_move = None
    optimal_score = None

    for action in actions(s):
        temp_state = copy.deepcopy(s)
        temp_state = make_move(temp_state, action, MAX_PLAYER)

        score = max_value(temp_state)
        if optimal_score is None or score > optimal_score:
            optimal_move = action
            optimal_score = score

    return optimal_move


#print(player(state))
#print(actions(state))
#print(terminal(state))
#print(utility(state))

play_mode2()
