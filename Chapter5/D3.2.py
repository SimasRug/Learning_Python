import  copy
game_over = False
# gameBoard = [' ',' ','0',' ',' ',' ','X',' ',' ']
# gameBoard = [   'X',' ','0',
#                 '0',' ',' ',
#                 '0','X','X']
gameBoard = [   ' ',' ',' ',
                ' ',' ',' ',
                ' ',' ',' ']
# gameBoard = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

def printboard(board):
    inc = 0
    for x in range(0,3):
        print(board[inc], '|', board[inc+1], '|', board[inc+2])
        inc = inc + 3


def check_avialble_position(board):
    arr = []
    for x in range(0,9):
        if(board[x] == ' '):
            arr.append(x)
    return arr

def check_for_win(board, player):
    wining_conditions = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for x in range (0,8):
        if(board[wining_conditions[x][0]] == player and board[wining_conditions[x][1]] == player and board[wining_conditions[x][2]] == player):
            return True
    return False


def computer_move(board, player):
    spot, position = minimax(board, player)
    # print('Reached')
    # return spot
    board[position] = player
    if check_for_win(board, player):
        print('Computer Won')
    return check_for_win(board, player), board

def minimax(board, player):
    available_spots = check_avialble_position(board)
    # print(len(available_spots))
    if(check_for_win(board, 'X')):
        return  (-10, -1)
    elif (check_for_win(board, '0')):
        return (10, -1)
    elif(available_spots == []):
        return (0, -1)

    if(player == '0'):
        best_value = -10000
        best_move = -1
        for x in available_spots:
            new_board = copy.deepcopy(board)
            new_board[x] = '0'
            # printboard(new_board)
            v, dummy = minimax(new_board, 'X')
            if(v > best_value):
                best_value = v
                best_move = x
        return (best_value, best_move)

    if(player == 'X'):
        best_value = 10000
        best_move = -1
        for x in available_spots:
            new_board = copy.deepcopy(board)
            new_board[x] = 'X'
            # printboard(new_board)
            v, dummy = minimax(new_board, '0')
            if(v < best_value):
                best_value = v
                best_move = x
        return (best_value, best_move)
            # print(available_spots[x])

    # return 'This should never return empty'

def player_move(board):
    # printboard(board)
    position = int(input('Enter position of X: '))
    state = False
    while not state:
        if(position < 10 and position > -1):
            avialble_positions = check_avialble_position(board)
            # print(avialble_positions)
            if(position in avialble_positions):
                board[position] = 'X'
                did_player_win = (check_for_win(board, 'X'))
                state = True
                if(did_player_win):
                    # printboard(board)
                    print('Player WON!')
                return did_player_win, board
            else:
                print('Position taken')
                return player_move(board)
        else:
            position = int(input('Enter position of X: '))



# printboard(gameBoard)
# print('\n')
printboard(gameBoard)
while not game_over:
    game_over, gameBoard = computer_move(gameBoard, '0')
    game_over, gameBoard = player_move(gameBoard)
    # input('')
    printboard(gameBoard)

    # printboard(gameBoard)
