board = [' ']*9
# board[3] = 0
# board[4] = 0
# board[5] = 0
mapping = {0:'X', 1:'0'}
winningConditions = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
game_over = False

def check_if_empty(position):
    if(board[position] == ' '):
        return True
    else:
        return False



def printBoard():
    a = 0
    for x in range(0,3):
        print(board[a], board[a+1], board[a+2])
        a = a + 3

def check_full_board():
    if(' ' in board):
        return false
    else:
        print('Nobody wins')
        return true


def player_put_value():
    put = False
    position = int(input('Enter the position that you want to place your X: '))

    while not put:
        if(0 <= position < 9 and check_if_empty(position) ):
            board[position] = 0
            put = True
            return board
        else:
            position = int(input('Enter the position that you want to place your X: '))

def check_for_win(player):
    for x in winningConditions:
        # print(x[0], x[1], x[2])
        if(board[x[0]] == player and board[x[1]] == player and board[x[2]] == player ):
            print('game won')
            return True
    return False



printBoard()
while not game_over:
    board = player_put_value()
    game_over = check_for_win(0)
    check_full_board();
    printBoard()
