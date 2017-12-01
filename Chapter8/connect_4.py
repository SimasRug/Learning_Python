def player_move():
    position = int(input('Enter position (1-7): '))
    if 0 < position > 8:
        # check if the position is available
    else:
        except ValueError ('Wrong input')

game_over = False
while not game_over:
    try:
        game_over = player_move()
    except ValueError as err_msg:
        print(err_msg,'\n')