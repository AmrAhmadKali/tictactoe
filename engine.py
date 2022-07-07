import numpy as np
import copy

DIMENSIONS = 3


def new_board():
    return [[None, None, None], [None, None, None], [None, None, None]]


def render(board):
    print('\t  |0  1  2')
    print('\t   _______')
    for i in range(DIMENSIONS):
        print('\t', i, end='|')
        for j in range(DIMENSIONS):
            if board[i][j] is not None:
                print(board[i][j], end='  ')
            else:
                print(' ', end='  ')

        print('')


def get_move():
    x_coord = int(input('X- coordinates : '))
    y_coord = int(input('Y- coordinates : '))

    return (x_coord, y_coord)


def make_move(board, coordinates, player):
    new_board = copy.deepcopy(board)
    new_board[coordinates[0]][coordinates[1]] = player
    return new_board


def is_valid_move(board, coordinates):
    if board[coordinates[0]][coordinates[1]] is None:
        return True
    return False


def player(board):
    count_x = sum([i.count('x') for i in board])
    count_o = sum([i.count('o') for i in board])

    if count_x - count_o == 1:
        return 'o'

    elif count_o - count_x == 1:
        return 'x'

    else:
        return 'x'


def get_winner(board):
    for i in range(DIMENSIONS):
        if board[i] == 3 * ['x']:          #Are any of the Rows are x
            return 'x'

        elif board[i] == 3 * ['o']:        #Are any of the Rows are o
            return 'o'
        vertical_temp = []
        for j in range(DIMENSIONS):
            vertical_temp.append(board[j][i])       #Generating lists of the singel Columns

        if vertical_temp == 3 * ['x']:          #Are any of the Rows are x
            return 'x'

        elif vertical_temp == 3 * ['o']:        #Are any of the Rows are o
            return 'o'

    main_diagonal_temp = np.diagonal(board)
    reverse_diagonal_temp = np.fliplr(board).diagonal()

    if all(main_diagonal_temp == (3 * ['x'])):  # Are any of the diagonals are x
        return 'x'

    elif all(reverse_diagonal_temp == (3 * ['x'])):    # Are any of the diagonals are x
        return 'x'

    elif all(main_diagonal_temp == 3 * ['o']):   # Are any of the diagonals are o
        return 'o'

    elif all(reverse_diagonal_temp == (3 * ['o'])):  # Are any of the diagonals are o
        return 'o'

    return False


def is_full(board):
    for i in board:
        for j in i:
            if j is None:
                return False
    return True


#Driver Code

def play_mode1():

    print('Wellcome in Tic Tac Toe \n ')   #TooDo

    current_board = new_board()
    render(current_board)

    while True:
        current_player = player(current_board)

        print(f'Player {current_player} turn')
        coord = get_move()

        if is_valid_move(current_board, coord):
            current_board = make_move(current_board, coord, current_player)

        else:
            print('Invalid move')
            continue

        render(current_board)

        winner = get_winner(current_board)

        if winner == 'x' or winner == 'o':     # TO Do
            break

        if is_full(current_board):
            break

#a = make_move([[None, 'X', None],[None, 'O', None],['O', 'X', None]], (0, 0), 'X')

#print(render(a))

#print(is_valid_move([[None, 'X', None],[None, 'O', None],['O', 'X', None]], (2, 0)))

#print(player([[None, 'x', None],['x', None, None],['o', 'x', 'o']]))

#get_winner([['x', 'o', 'o'],[None, 'o', 'x'],['o', None, 'x']])

