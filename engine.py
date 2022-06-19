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

def make_move(board, coordintes, player):
    new_board = board
    new_board[coordintes[0]][coordintes[1]] = player
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
    for i in board:
        if i == 3 * ['x']:
            print ('x is winner')
            return 'x'
        elif i == 3 * ['o']:
            print('o is winner')
            return 'o'

    for i in range(DIMENSIONS):
        for j in range(DIMENSIONS):
            temp = 3 * board[j][i]
            if temp == 3 * ['x']:
                print ('x is winner')
                return 'x'
            elif temp == 3 * ['o']:
                print('o is winner')
                return 'o'
a = make_move([[None, 'X', None],
         [None, 'O', None],
         ['O', 'X', None]], (0, 0), 'X')

#print(render(a))

#print(is_valid_move([[None, 'X', None],[None, 'O', None],['O', 'X', None]], (2, 0)))

print(player([[None, 'x', None],
         ['x', None, None],
         ['o', 'x', 'o']]))
