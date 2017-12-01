import copy

w, h = 6, 6;
game_board = [[0 for x in range(w)] for y in range(h)] 



def print_board(board):
    for x in range(0, len(board)):
       for j in range(0, len(board[x])):
            print('|', board[x][j], '|', end=' ')
            if(j == h - 1):
                print()

def check_available_spots(board):
    free_positions = []
    for x in range(0, len(board)):
        for j in range(0,len(board[x])):
            if(board[x][j] == 0):
                free_positions.append([x,j])
    return free_positions

def check_for_win(board, player):
    #horizontal check
    for j in range(0, len(board)-4):
        for x in range(0, len(board[j])):
            if(board[x][j] == player and board[x][j+1] == player and board[x][j+2] == player and board[x][j+3] == player and board[x][j+4] == player):
                # print('Horizontal win')
                return True
    
    #vertical check
    for x in range(0, len(board)-4):
        for j in range(0, len(board)):
            if(board[x][j] == player and board[x+1][j] == player and board[x+2][j] == player and board[x+3][j] == player and board[x+4][j] == player):
                # print('Vertical win')
                return True

    for x in range(4, len(board)):
        for j in range(0, len(board[x])-4 ):
            if(board[x][j] == player and board[x-1][j+1] == player and board[x-2][j+2] == player and board[x-3][j+3] == player and board[x-4][j+4] == player):
                # print('Asceding diagonal win')
                return True            

    for x in range(4, len(board)):
        for j in range(0, len(board[x])):
            if(board[x][j] == player and board[x-1][j-1] == player and board[x-2][j-2] == player and board[x-3][j-3] == player and board[x-4][j-4] == player):
                # print('Descending diagonal win')
                return True
    return False



def check_for_tie(board):
    available_spots = check_available_spots(board)
    if(available_spots == []):
        return True
    return False


def player_move(board, player):
    positionX, positionY = map(int, input('Input the position: ').split())
    available_positions = check_available_spots(board)
    state = False

    while not state:

        if(-1 < positionX < w and -1 < positionY < h):

            if([positionX,positionY] in available_positions):
                board[positionX][positionY] = player
                did_player_win = check_for_win(board, player)
                is_it_tie = check_for_tie(board)

                if(is_it_tie and not did_player_win):
                    print('TIE!!!')
                    return is_it_tie, board
                else:
                    if(did_player_win):
                        print('player ', player, ' won')
                        return did_player_win, board

                state = True
                return False, board

            else:
                print('Position taken')
                positionX, positionY = map(int, input('Input the position: ').split())

        else:
            print('Input out of range')
            positionX, positionY = map(int, input('Input the position: ').split())



def computer_move(board, player):

    # score, move = minimax(board, player)
    minimax(board, player)
    # print(score, move)
    # board[move[0]][move[1]] = player

    is_it_tie = check_for_tie(board)
    check_win = check_for_tie(board)

    if(is_it_tie and not check_win):
        print('TIE!!!')
        return is_it_tie, board
    else:
        if(check_win):
            print('Computer Won!')
        return check_win, board
    # print('in comp move')
    # return True, board


def minimax(board, player):

    available_spots = check_available_spots(board)
    print(len(available_spots))
    print(player)

    if(check_for_win(board, 'X')):
        return(-10, [None,None])
    elif(check_for_win(board,'Y')):
        return(10, [None,None])
    elif(available_spots == []):
        return(0, [None,None])

    if(player == 'Y'):
        best_value = -1000
        best_move = [None,None]
        for x in available_spots:
            new_board = copy.deepcopy(board)
            new_board[x[0]][x[1]] = 'Y'
            print_board(new_board)
            value, move = minimax(new_board, 'Y')

            if(value > best_value):
                best_value = value
                best_move = x
                # print(best_move_arr)
        return best_value, best_move

    if(player == 'X'):
        best_value = 1000
        best_move = [None, None]
        for x in available_spots:
            new_board = copy.deepcopy(board)
            new_board[x[0]][x[1]] = 'X'
            print_board(new_board)
            value, move = minimax(new_board, 'Y')

            if(value < best_value):
                best_value = value
                best_move = x
        return best_value, best_move



    # return 0, 0






game_over = False
# game_board[None][None] = 'Y'
print_board(game_board)
while game_over == False:

    # if(game_over == False):
    #     game_over, game_board = player_move(game_board, 'X')
    #     print_board(game_board)
    #     print()

    if(game_over == False):
        game_over, game_board = computer_move(game_board, 'Y')
        print_board(game_board)
        print()
    input()




# game_board[0][9]