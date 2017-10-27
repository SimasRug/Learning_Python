# Python program to display calendar of given month of the year

# import module
import calendar

# yy = 2014
# mm = 11

# To ask month and year from the user
yy = int(input("Enter year: "))
mm = int(input("Enter month: "))
leap = ''

if mm == 2:
    if(yy % 4 == 0) and (not (yy % 100 == 0) or (yy % 400 == 0)):
        leap = 'Was a leap year'


# display the calendar
print('\n',calendar.month(yy, mm),'\n', leap)
