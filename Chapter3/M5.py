print('This program will determine if your car needs an oidl change')

miles_between_changes = 7500
miles_warning = 500
valid_entries = False


while not valid_entries:
    mileage_last_oilchange = int(input('Enter mileage of last oil change: '))
    current_mileage =  int(input('Enter current mileage: '))

    if current_mileage < mileage_last_oilchange:
        print('Invalid entry current mileage cant be less then last oil change')
    else:
        miles_traveled = current_mileage - mileage_last_oilchange
        valid_entries = True


miles_left = miles_between_changes - miles_traveled

if miles_traveled >= miles_between_changes:
    print('You are do for an oil change')
    print('You are', -miles_left, 'miles overdue')
elif miles_traveled >= miles_between_changes - miles_warning:
    print('You will soon be do for an oil change')
    print('Chnage you oi in', miles_left, 'miles')
else:
    print('You are not in need of a oil change')
    print('Chnage you oi in', miles_left, 'miles')
