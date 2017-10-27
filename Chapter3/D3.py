house = int(input('How much did you house cost?: '))
income = int(input('Whats you combined income?: '))
owned = input('Have you owned other property in the last 3 years?:')


if house < 800000 and income < 225000 and (owned == 'No' or owned == 'no' or owned == 'NO'):
    print('You apply for the credit')
else:
    print('You dont apply for the credit')
