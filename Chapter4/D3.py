<<<<<<< HEAD
board = []

for i in range(0, 5):
    board.append("0"*5)

print(board)
=======
import random

def draw_board(): #createe the battleship board
    board = []
    for x in range (0,5):
        board.append([])
        for i in range (0,5):
            board[x].append(0)
    return board

def display_board(board): # display the board
    for x in board:
        print(x)

def place_ships(i,j, board): # assign ship positions for ships
    positions = []
    for x in range(i,j):
        condition = False
        while condition == False:
            user_v = int(input('Input ships vertical position: '))
            user_h = int(input('Input ships horizontal position: '))
            if(board[user_v][user_h] == 0):
                board[user_v][user_h] = 'S'
                display_board(board)
                condition = True
            else:
                print('Wrong input a shihp is alredy placed there')
    return board

def comp_shot(board, over): #Computer shoots at board
    global game_over
    if(over == False):
        shot_v = random.randint(0,4) # get random numbers
        shot_h = random.randint(0,4)

        if(board[shot_v][shot_h] == 0):
            print('Computer shot missed')
            board[shot_v][shot_h] = 'X'

        elif(board[shot_v][shot_h] == 'S'):
            print('Computer hit your ship')
            board[shot_v][shot_h] = 'H'
            if(check_game_over(board)): # call a function that looks if ther are any ships left
                comp_shot(board, over)
            else:
                game_over = True
                print('Game over, computer Won')

        elif(board[shot_v][shot_h] == 'X' or board[shot_v][shot_h] == 'H'):
            if(check_full_board(board)): #check if theres any more spaces left on the board
                comp_shot(board, over)
            else:
                game_over = True

    else:
        print('Game Over')
    return board

def check_game_over(board): #check if there's ships left
    value = False
    for x in board:
        if('S' in x):
            value = True
    return value

def check_full_board(board):
    value = False
    for x in board:
        if( 0 in x):
            value = True
    return value

def computer_place(board):
    shot_v = random.randint(0,4) # get random numbers
    shot_h = random.randint(0,4)
    if(board[shot_v][shot_h] == 'H'):
        computer_place(board)
    else:
        length = len(board)
        # print(length)
        position = random.randint(0,1)
        if(position == 1): #vertical
            if(shot_v > length/2):
                num = shot_v
                for x in range (0,3):
                    board[num][shot_h] = 'S'
                    num  = num - 1
            else:
                num = shot_v
                for x in range (0,3):
                    board[num][shot_h] = 'S'
                    num  = num + 1

        else: #horizontal
            # print(shot_v, shot_h)
            if(shot_h > length/2):
                num = shot_h
                for x in range (0,3):
                    board[shot_v][num] = 'S'
                    num  = num - 1
            else:
                num = shot_h
                for x in range (0,3):
                    board[shot_v][num] = 'S'
                    num  = num + 1
    return board


def human_shoot_computer(board, user_display):
    global game_over
    user_v = int(input('Input ships vertical position: '))
    user_h = int(input('Input ships horizontal position: '))
    if(board[user_v][user_h] == 0):
        board[user_v][user_h] = 'X'
        user_display[user_v][user_h] = 'X'
        display_board(user_display)

    elif(board[user_v][user_h] == 'S'):
        print('You hit computers ship')
        board[user_v][user_h] = 'H'
        user_display[user_v][user_h] = 'H'
        draw_board(user_display)

        if(check_game_over(board)): # call a function that looks if ther are any ships left
            human_shoot_computer(board, user_display)
        else:
            game_over = True
            print('Game over, Human Won')

    elif(board[user_v][user_h] == 'X' or board[user_v][user_h] == 'H' ):
            if(check_full_board(board)): #check if theres any more spaces left on the board
                human_shoot_computer(board, user_display)
            else:
                game_over = True
    return board

game_over = False

print('Stat Game')

player_board = draw_board()
computer_board = draw_board()
place_ships(0,3,player_board)
computer_board_for_user = draw_board()
computer_board = computer_place(computer_board)

print('\n')
print('Human Board')
display_board(player_board)
print('Computer Board')
display_board(computer_board_for_user)
print('\n')


while game_over == False:
    print('Shoot computers ship')
    human_shoot_computer(computer_board, computer_board_for_user )
    comp_shot(player_board, game_over)
    print('Human Board')
    display_board(player_board)
    print('Computer Board')
    display_board(computer_board_for_user)
    print('\n')
>>>>>>> f1651ace078485599c60da935f83206e000d9b27
