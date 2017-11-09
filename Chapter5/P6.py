def getContinue():
    cond = False
    while not cond:
        a = input('Do you want to continue: ')
        if(a in ('n', 'N', 'y', 'Y')):
            a = a.lower()
            cond = True
            return a

print(getContinue())
