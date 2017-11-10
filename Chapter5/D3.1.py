# gameBoard = [' ']*9
# gameBoard = ['X','X','X',' ',' ',' ',' ',' ',' ']

gameBoard = ['0',' ','X','X','X',' ',' ','0','0']


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



def player_move(board):
    printboard(board)
    position = int(input('Enter position of X: '))
    state = False
    while not state:
        if(position < 9 and position > -1):
            avialble_positions = check_avialble_position(board)
            # print(avialble_positions)
            if(position in avialble_positions):
                board[position] = 'X'
                did_player_win = (check_for_win(board, 'X'))
                state = True
                if(did_player_win):
                    printboard(board)
                    print('Player WON!')
                return did_player_win, board
            else:
                print('Position taken')
                return player_move(board)
        else:
            position = int(input('Enter position of X: '))


def computer_move(board):
    print('Computer Turn')
    printboard(board)
    find_best_move(board, '0')

    # avialble_positions = check_avialble_position(board)
    # print(avialble_positions)
    # for x in range(0, len(avialble_positions)):
    #     board[avialble_positions[x]] = '0'
    #     printboard(board)
    #     did_computer_win = check_for_win(board,'0')
    #     print(did_computer_win)
    #     print('\n')
    #     if(did_computer_win):
    #         print('Computer Win!')
    #         return
    #     else:
    #         print('Computer did not win!!')
    #         computer_move(board)


def find_best_move(board, player):
    possible_moves = []
    avialble_positions = check_avialble_position(board)
    for x in range(0, len(avialble_positions)):
        new_board = list(board)
        new_board[avialble_positions[x]] = player
        did_computer_win = check_for_win(new_board,player)






    # print(possible_moves)
    # for x in possible_moves:
    #     printboard(x)
    #     print('\n')








game_over = False;
while not game_over:
     game_over, gameBoard = player_move(gameBoard)
     print(game_over, gameBoard)
     # gameover, gameBoard = computer_move(gameBoard)
# check_for_win(gameBoard, 'X')
# computer_move(gameBoard)
