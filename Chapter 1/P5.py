cities = int(input('How many cities? '))

num = 1
citiesTemp = cities

while citiesTemp >=1:
    num = num * citiesTemp
    citiesTemp = citiesTemp - 1

    

print('For ', cities, ' there are ', num, ' possible routes')
