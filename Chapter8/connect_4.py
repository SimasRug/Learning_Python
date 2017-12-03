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


def check_available_postion(board):
    free_positions = []
    for x in range(0, len(board)):
        for j in range(0,len(board[x])):
            if(board[x][j] == 0):
                free_positions.append([x,j])
    return free_positions
        
       
           
            
    


def player_move(board):
    position = int(input('Enter position (1-7): '))
    if 0 < position and position < 8:
        position = position - 1
        if(board[0][position] != 0):
            print('Position taken')
            player_move(board)
        else:
            needed_comlumn = []
              
            available_positions = check_available_postion(board)

            for x in available_positions:
                if(x[1] == position):
                    needed_comlumn.append(x)
            
            fall_move = -1
            for x in needed_comlumn:
                # print (x)
                if(x[0] > fall_move):
                    fall_move = x[0]

            board[fall_move][position] = 1
                
            return False, board

    else:
      raise ValueError ('Wrong input')


game_over = False
while not game_over:
    try:
        game_over, game_board = player_move(game_board)
    except ValueError as err_msg:
        print(err_msg,'\n')

    print_board(game_board)