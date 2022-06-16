
state = [[None, None, None],
         [None, None, None],
         [None, None, None]] #initial board

def player(s):
    count = 1
    if count % 2 == 0:
        count = count + 1
        return 'O'
    else:
        count = count + 1
        return 'X'

def action(s, player: str):
    moves = set()

    for i in s:             #rows
        for j in i:         #columns
            if j is None:
                moves.add((i,j))

    return moves