import random
from random import randint
import copy
from copy import deepcopy


width, height = 7, 6
game_board = [[0 for x in range(width)] for y in range(height)]
values = {0: ' ', 1: 'R', 2: 'Y'}

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
           



           

def player_move(board, player):
    position = int(input('Enter position (1-7): '))
    if 0 < position and position < 8:
        position = position - 1
        available_col = check_available_positions(board)
        if(position not in available_col):
            print('Position taken')
            return player_move(board, player)
        else:
            needed_comlumn = []
            test = False
            incrament_me = 0
            while not test:
                
                
        return False, board
        #  if(board[0][position] != 0):
        #     print('Position taken')
        #     return player_move(board, player)
        # else:
        #     needed_comlumn = []
              
        #     available_positions = check_available_positions(board)

        #     for x in available_positions:
        #         if(x[1] == position):
        #             needed_comlumn.append(x)
            
        #     fall_move = -1
        #     for x in needed_comlumn:
        #         if(x[0] > fall_move):
        #             fall_move = x[0]

        #     board[fall_move][position] = player

        #     if(check_for_win(board, player)):
        #         return True, game_board
        #     elif(len(check_available_positions(board)) == 0):
        #         print('Tie Game')
        #         return True, game_board
        #     return False, board
    else:
      raise ValueError ('Wrong input')


def check_for_win(board, player):
    # height 6 for arr +1 width 7 for arr +1

    for j in range(0, 6):
        for x in range(0, 4):
            if(board[j][x] == player and board[j][x+1] == player and board[j][x+2] == player and board[j][x+3] == player):
            # print(board[j][x])
                print('Horizontal win')
                return True
    
    # vertical check
    for x in range(0, 3):
        for j in range(0,7):
            if(board[x][j] == player and board[x+1][j] == player and board[x+2][j] == player and board[x+3][j] == player):
                print('Vertical win')
                return True

    for x in range(3,6):
        for j in range(3,7):
            if(board[x][j] == player and board[x-1][j-1] == player and board[x-2][j-2] == player and board[x-3][j-3] == player):
                print('Diagonal win')
                return True
    
    for x in range(3,6):
        for j in range(0,4):
            if(board[x][j] == player and board[x-1][j+1] == player and board[x-2][j+2] == player and board[x-3][j+3]):
                print('Diagonal win')
                return True
    return False


def computer_move(board, player):
    val, mov = minimax(board, player)
    print(val, mov)
    # board[mov[0]][mov[1]] = player
    # if(check_for_win(board, player)):
    #     return True, game_board
    # elif(len(check_available_positions(board)) == 0):
    #     print('Tie Game')
    #     return True, game_board    
    return False, board


def minimax(board, player):
    available_positions = check_available_positions(board)
    # available_positions.reverse()

    if(check_for_win(board, 1)):
        return (-10, [-1,-1])
    elif(check_for_win(board,2)):
        return (10, [-1,-1])
    elif(available_positions == []):
        return (0, [-1,-1])

    if(player == 2):
        best_value = -1000
        best_move = [-1,-1]
        print(player, best_move, best_value)
        for x in available_positions:
            new_board = copy.deepcopy(board)
            new_board[x[0]][x[1]] = player
            print(new_board, '\n')
            value, move = minimax(new_board, 2)

            if(value > best_value):
                best_value = value
                best_move = [x[0],x[1]]
                print([x[0],x[1]])
        return best_value, best_move
    


    # return (0,[-1,-1])


game_over = False
print_board(game_board)
while not game_over:
    if not game_over:
        try:
            game_over, game_board = player_move(game_board, 1)
        except ValueError as err_msg:
            print(err_msg,'\n')
        print_board(game_board)

    # if not game_over:
    #     try:
    #         game_over, game_board = computer_move(game_board, 2)
    #     except ValueError as err_msg:
    #         print(err_msg,'\n')

        # print_board(game_board)