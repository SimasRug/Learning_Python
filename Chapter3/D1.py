def weight():
    print('For converting pounds to grams enter 1')
    selection = int(input('For converting grams to punds enter 2: \n'))

    if selection == 1:
        pounds = float(input('Input pounds: '))
        total = pounds * 453.59
        print(pounds,' pounds are ',total, 'grams')
    else:
        grams = float(input('Input grams: '))
        total = format(grams / 453.59, '.4f')
        print(grams,' grams are ',total, 'pounds')


def distance():
    print('Do you want to convert short or long distances?')
    choice = input('S for short L for long: ')

    if choice == 'S':
        print('For converting inches to centimeters enter 1')
        selection = int(input('For converting centimeters to inches enter 2: \n'))
        if selection == 1:
            inches = float(input('Input inches: '))
            total = inches * 2.54
            print(inches,' inches are ',total, 'centimeters')
        elif selection == 2:
            cm = float(input('Input centimeters: '))
            total = format(cm / 2.54, '.4f')
            print(cm,' centimeters are ',total, 'inches')
    elif choice == 'L':
        print('For converting kilometers to miles enter 1')
        selection = int(input('For converting miles to kilometers enter 2: \n'))
        if selection == 1:
            km = float(input('Input kilometers: '))
            total = km / 1.6
            print(km,' kilometers are ',total, 'miles')
        elif selection == 2:
            miles = float(input('Input miles: '))
            total = miles * 1.6
            print(miles,' miles are ',total, 'kilometers')





print('What do you want ot convet?')
choice = input('For weight enter W for distance enter D: ')

while choice not in ('W', 'D'):
    choice = input('For weight enter W for distance enter D: ')


if choice == 'W':
    weight()
elif choice == 'D':
    distance()
