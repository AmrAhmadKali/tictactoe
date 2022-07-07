import json

# difine a dictionary
dict1 =
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

    if winner == 'x' or winner == 'o':     
        break

    if is_full(current_board):
        print('It is a Tie')
        break
        
        # load the json data
out_file = open ("raed_json.py", "w")
json.dump(dict1, out_file. indent = 6)

out_file.close()
        
