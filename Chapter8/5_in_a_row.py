w, h = 10, 10;
game_board = [[0 for x in range(w)] for y in range(h)] 



def print_board(board):
   for x in range(0, len(game_board)):
       for j in range(0, len(game_board[x])):
            print('|', game_board[x][j], '|', end=' ')
            if(j == 9):
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
    for x in range(0, len(board)-4):
        for j in range(0, len(board[x])):
            if(board[x][j] == player and board[x][j+1] == player and board[x][j+2] == player and board[x][j+3] == player and board[x][j+4] == player):
                print('HorizONTAL WIN')
                return True




def player_move(board, player):

    positionX, positionY = map(int, input('Input the position: ').split())
    available_positions = check_available_spots(board)
    state = False

    while not state:

        if(-1 < positionX < 10 and -1 < positionY < 10):

            if([positionX,positionY] in available_positions):
                board[positionX][positionY] = player
                did_player_win = check_for_win(board, player)
                if(did_player_win):
                    print('player x won')
                    return did_player_win, board
                state = True
                return False, board

            else:
                print('Position taken')
                positionX, positionY = map(int, input('Input the position: ').split())

        else:
            print('Input out of range')
            positionX, positionY = map(int, input('Input the position: ').split())


# game_over = False
# print_board(game_board)
# while game_over == False:
#     game_over, game_board = player_move(game_board, 'X')
#     print_board(game_board)
print(game_board[0][9])