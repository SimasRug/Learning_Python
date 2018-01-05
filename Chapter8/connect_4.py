import random
from random import randint
import copy
from copy import deepcopy
import time


width, height = 7, 6
# game_board = [[0 for x in range(width)] for y in range(height)]
game_board = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
# game_board = [[0,0,0,0,0,0,0],[0,0,0,1,2,1,1],[1,2,1,2,2,1,2],[2,1,2,1,1,2,1],[2,1,2,2,1,1,1],[1,2,1,2,1,2,1]]

values = {0: ' ', 1: 'R', 2: 'Y', 3:'W'}

def print_board(board):
    print('  1    2    3    4    5    6    7')
    for x in range(len(board)):
        for j in range(len(board[x])):
            print('|', values[board[x][j]], '|', end='')
            if j == height:
                print()


def check_available_positions(board):
    free_positions = []
    for x in range (0, len(board[0])):
        if(board[0][x] == 0):
            free_positions.append(x)
    return free_positions
           

def drop(board, player, pos):
    new_board = deepcopy(board)
    stopLoop = False
    increment_me = 0
    while not stopLoop:
        if(increment_me == 5 and new_board[increment_me][pos] == 0):
            new_board[increment_me][pos] = player
            stopLoop = True
        else:
            if(new_board[increment_me + 1][pos] == 0):
                increment_me = increment_me + 1
            else:
                new_board[increment_me][pos] = player
                stopLoop = True
    
    return new_board


           

def player_move(board, player):
    position = int(input('Enter position (1-7): '))
    if 0 < position and position < 8:
        position = position - 1
        available_col = check_available_positions(board)

        if(position not in available_col):
            print('Position taken')
            return player_move(board, player)
        else:
            board = drop(board, player, position)
            if(check_for_win(board, player)):
                print('player wins')
                return True, board
            elif(len(check_available_positions(board)) == 0):
                print('Tie game')
                return True, board            
        return False, board
    else:
      raise ValueError ('Wrong input')


def check_for_win(board, player):
    # height 6 for arr +1 width 7 for arr +1

    for j in range(0, 6):
        for x in range(0, 4):
            if(board[j][x] == player and board[j][x+1] == player and board[j][x+2] == player and board[j][x+3] == player):
                board[j][x] = 3
                board[j][x+1] = 3
                board[j][x+2] = 3
                board[j][x+3] = 3
                return True
    
    # vertical check
    for x in range(0, 3):
        for j in range(0,7):
            if(board[x][j] == player and board[x+1][j] == player and board[x+2][j] == player and board[x+3][j] == player):
                board[x][j] = 3
                board[x+1][j] = 3
                board[x+2][j] = 3
                board[x+3][j] = 3
                return True

    for x in range(3,6):
        for j in range(3,7):
            if(board[x][j] == player and board[x-1][j-1] == player and board[x-2][j-2] == player and board[x-3][j-3] == player):
                board[x][j] = 3
                board[x-1][j-1] = 3
                board[x-2][j-2] = 3
                board[x-3][j-3] = 3
                # print('Diagonal win')
                return True
    
    for x in range(3,6):
        for j in range(0,4):
            if(board[x][j] == player and board[x-1][j+1] == player and board[x-2][j+2] == player and board[x-3][j+3] == player):
                board[x][j] = 3
                board[x-1][j+1] = 3
                board[x-2][j+2] = 3
                board[x-3][j+3] = 3
                # print('Diagonal win')
                return True
    return False

def check_good_position(board, player):
    # height 6 for arr +1 width 7 for arr +1
    for j in range(0, 6):
        for x in range(0, 4):
            if(board[j][x] == 0 and board[j][x+1] == player and board[j][x+2] == player and board[j][x+3] == 0):
                # print('Good horizontal moves')
                return True
    
    # # vertical check
    # # for x in range(0, 3):
    # #     for j in range(0,7):
    # #         if(board[x+1][j] == player and board[x+2][j] == player and board[x+3][j] == player):
    # #             return True
   

    # for x in range(3,6):
    #     for j in range(3,7):
    #         if(board[x][j] == 0 and board[x-1][j-1] == player and board[x-2][j-2] == player and board[x-3][j-3] == player):
    #             # print('Good diagonal move')
    #             return True
    
    # for x in range(3,6):
    #     for j in range(0,4):
    #         if(board[x][j] == 0 and board[x-2][j+2] == player and board[x-3][j+3] == player):   
    #             # print('Good vertical moves')
    #             return True
    return False

def computer_move(board, player):
    start = time.time()
    val, mov = minimax(board, player, -1000, 1000, 8)
    end = time.time()
    print('Time: ',end - start)
    # val, mov = minimax(board, player)
    # print(val,mov)
    # board[mov[0]][mov[1]] = player
    board = drop(board,player,mov)

    if(check_for_win(board, player)):
        print('Computer wins')
        return True, board
    elif(len(check_available_positions(board)) == 0):
        print('Tie game')
        return True, board

    return False, board

def minimax(board, player, alpha, beta, depth):
    available_positions = check_available_positions(board)
    random.shuffle(available_positions)
    # print(depth)

    if(depth == 0):
        return(0,-1)
    elif(check_for_win(board,1)):
        return(-10,-1)
    elif(check_for_win(board,2)):
        return (10, -1)
    # elif(check_good_position(board,1)):
    #     return(-5,-1)
    # elif(check_good_position(board,2)):
    #     return(5,-1)
    elif(available_positions == []):
        return (0, -1)

    if(player == 2):
        best_value = -1000
        best_move = -1
        for x in available_positions:
            new_board = deepcopy(board) #put in a function
            new_board = drop(new_board,2,x)
            value, move = minimax(new_board,1, alpha, beta, depth-1)

            if(value > best_value):
                best_value = value
                best_move = x
            alpha = max(alpha, best_value)
            if beta <= alpha:
                break
        return best_value, best_move

    if(player == 1):
        best_value = 1000
        best_move = -1
        for x in available_positions:
            new_board = deepcopy(board)
            new_board = drop(new_board,1,x)
            value, move = minimax(new_board,2, alpha, beta, depth-1)

            if(value < best_value):
                best_value = value
                best_move = x
            beta = min(beta, best_value)
            if beta <= alpha:
                break
        return best_value, best_move

# def minimax(board, player):
#     available_positions = check_available_positions(board)

#     if(check_for_win(board,1)):
#         return(-10,-1)
#     elif(check_for_win(board,2)):
#         return (10, -1)
#     elif(available_positions == []):
#         return (0, -1)

#     if(player == 2):
#         best_value = -1000
#         best_move = -1
#         for x in available_positions:
#             new_board = deepcopy(board) #put in a function
#             new_board = drop(new_board,2,x)
#             value, move = minimax(new_board,1)

#             if(value > best_value):
#                 best_value = value
#                 best_move = x
#         return best_value, best_move

#     if(player == 1):
#         best_value = 1000
#         best_move = -1
#         for x in available_positions:
#             new_board = deepcopy(board)
#             new_board = drop(new_board,1,x)
#             value, move = minimax(new_board,2)

#             if(value < best_value):
#                 best_value = value
#                 best_move = x
#         return best_value, best_move





game_over = False
print_board(game_board)

while not game_over:
    if not game_over:
        try:
            game_over, game_board = computer_move(game_board, 2)
        except ValueError as err_msg:
            print(err_msg,'\n')
        print_board(game_board)

    if not game_over:
        try:
            game_over, game_board = player_move(game_board, 1)
        except ValueError as err_msg:
            print(err_msg,'\n')

        print_board(game_board)








