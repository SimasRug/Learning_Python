import copy

gameBoard = ['0',' ','X','X','X',' ',' ','0','0']

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

def score(board):
    if(check_for_win(board,'0')):
        return {score: -10}
    elif(check_for_win(board,'X')):
        return {score: 10}
    elif(len(check_avialble_position(board)) == 0):
        return {score: 0}


def printboard(board):
    inc = 0
    for x in range(0,3):
        print(board[inc], '|', board[inc+1], '|', board[inc+2])
        inc = inc + 3

def minimax(board, player):
    return score()



printboard(gameBoard)
print('\n')
minimax(gameBoard,'X')

https://github.com/omegadeep10/tic-tac-toe/blob/master/game.py
