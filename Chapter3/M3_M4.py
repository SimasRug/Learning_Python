print('This program will display the number of days in a given month')

valid_input = True

month = int(input('Enter the month (1-12): '))

while 0 >= month or month >= 13:
    month = int(input('Enter the month (1-12): '))



if month == 2:
    year = int(input('Please enter the year: '))

    if(year % 4 == 0) and (not (year % 100 == 0) or (year % 400 == 0)):
        num_days = 29
    else:
        num_days = 28
elif month in (1, 3, 5, 7, 8, 10, 12):
    num_days = 31

elif month in (4, 6, 9, 11):
    num_days = 30

else:
    print('* Invalid Value Entered - ', month, '*') #this kinda usless now
    valid_input = False

if valid_input:
    if num_days == 29:
        print('There are ', num_days, ' days in month (a leap year)')
    else:
        print('There are ', num_days, ' days in month')
