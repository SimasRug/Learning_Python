total = 0;
user_list = int(input('How many numbers do you want to enter?: '))

for x in range (0,user_list):
    n = int(input('Enter possitive integers: '))
    if(n < 100):
        total = total + n



print('Your entered numbers sum is: ', total)
