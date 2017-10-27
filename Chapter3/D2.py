current_year = int(input('Enter current year: '))
future_year = int(input('Enter future year: '))


count_for_loop = future_year - current_year

for i in range (0, count_for_loop):
     if(current_year % 4 == 0) and (not (current_year % 100 == 0) or (current_year % 400 == 0)):
         print(current_year, 'is leap year')
     current_year = current_year + 1
