def printAsteriks(n):
    if(n > 0):
        if(n > 75):
            for x in range (0, 75):
                print('*', end='')
        else:
            for x in range (0, n):
                print('*', end='')


printAsteriks(100)
