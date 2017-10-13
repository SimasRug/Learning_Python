import math
cities = int(input('Enter the number of cities: '))


num = math.factorial(cities)

calc_sec = round(num / 1000000)
sec_to_year =(calc_sec/(365*24*60*60))

print('To brute force the shortest distance between ', cities, ' cities it would take ', sec_to_year,' years')
