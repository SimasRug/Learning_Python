import random


print('Add up to the displayded terget value')
print('Enter values  as 1, 5, 10, 25, 50')
print('----------------')

def calcSteps(amount):
    steps = 0
    while amount > 0:
        if amount >= 50:
            amount = amount - 50
            steps = steps + 1
        elif amount >= 25:
            amount = amount - 25
            steps = steps + 1
        elif amount >= 10:
            amount = amount - 10
            steps = steps + 1
        elif amount >= 5:
            amount = amount - 5
            steps = steps + 1
        elif amount >= 1:
            amount = amount - 1
            steps = steps + 1
    return steps


terminate = False
empty_str = ''

while not terminate:
    amount = 16 #random.randint(1,99)
    print('enter numbers that add up to', amount)
    game_over = False
    total = 0
    steps = calcSteps(amount)
    step_count = 0

    while not game_over:
        valid_entrie = False

        while not valid_entrie:
            if total == 0:
                entry = input('Make first entry: ')
                step_count = step_count + 1
            else:
                entry = input('Make next entry: ')
                step_count = step_count + 1

            if entry in ( empty_str, '1', '5', '10', '25', '50'):
                valid_entrie = True

        if entry == empty_str or step_count > steps + 1 :

            if step_count > steps + 1:
                print('You made to many entries for optimal count')

            elif total == amount:
                print('Correct')
            else:
                print('Sorry you only entered: ', total)

            game_over = True
        else:
            total = total + int(entry)
            if total > amount:
                print('Total amount exeeds', amount)
                game_over = True

        if game_over:
            entry = input('\n Try again? \n')

            if entry == 'n':
                terminate = True
print('thanks for playing')
