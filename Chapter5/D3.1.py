import copy
import random

game_over = False
game_board = [' ']*9

def print_board(board):
    inc = 0
    for x in range(0,3):
        print(board[inc], '|', board[inc+1], '|', board[inc+2])
        inc = inc + 3

def check_available_spots(board):
    free_positions = []
    for x in range(0, len(board)):
        if(board[x] == ' '):
            free_positions.append(x)
    return free_positions

def check_for_win(board, player):
    wining_conditions = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for x in range (0,8):
        if(board[wining_conditions[x][0]] == player and board[wining_conditions[x][1]] == player and board[wining_conditions[x][2]] == player):
            return True
    return False

def check_for_Tie(board):
    available_positions = check_available_spots(board)
    if( available_positions == []):
        return True
    return False

def player_move(board, player):
    position = int(input('Enter position of {}: '.format(player)))
    state = False
    while not state:
        if(position > -1 and position < 9):
            available_positions = check_available_spots(board)
            if(position in available_positions):
                board[position] = player
                is_it_tie = check_for_Tie(board)
                did_player_win = check_for_win(board, player)
                state = True
                if(is_it_tie and not did_player_win ):
                    print('TIE!!')
                    return is_it_tie ,board
                else:
                    if(did_player_win):
                        print('Player {} WON!!!'.format(player))
                    return did_player_win, board
            else:
                print('This position is taken')
                position = int(input('Enter position of {}: '.format(player)))
                # return player_move(board, player)
        else:
            print('Wrong Input')
            position = int(input('Enter position of {}: '.format(player)))

def computer_move(board, player):
    score, move = minimax(board, player)
    board[move] = player
    is_it_tie = check_for_Tie(board)
    check_win = check_for_win(board, player)
    if(is_it_tie and not check_win):
        print('TIE!!')
        return is_it_tie, board
    else:
        if(check_win):
            print('Computer Won!!!')
        return check_win, board


def minimax(board, player):
    available_spots = check_available_spots(board)
    # print(available_spots)
    random.shuffle(available_spots)
    # print(available_spots)
    

    if(check_for_win(board, 'X')):
        return (-10, -1)
    elif(check_for_win(board, '0')):
        return (10, 1)
    elif(available_spots == []):
        return (0, -1)

    if(player == '0'):
        best_value = -1000
        best_move = -1
        for x in available_spots:
            new_board = copy.deepcopy(board)
            new_board[x] = '0'
            value, move = minimax(new_board, 'X')

            if(value > best_value):
                best_value = value
                best_move = x
                # print(best_move_arr)
        return best_value, best_move

    if(player == 'X'):
        best_value = 1000
        best_move = -1
        for x in available_spots:
            new_board = copy.deepcopy(board)
            new_board[x] = 'X'
            value, move = minimax(new_board, '0')

            if(value < best_value):
                best_value = value
                best_move = x
        return best_value, best_move



print_board(game_board)
print()
while game_over == False:

    if(game_over == False):
        game_over, game_board = player_move(game_board, 'X')
        print_board(game_board)
        print()

    if(game_over == False):
        game_over, game_board = computer_move(game_board, '0')
        print_board(game_board)
        print()

