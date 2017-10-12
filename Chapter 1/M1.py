p = f = i = c = 1
R = 7
n = int(input('How many planets per start can support life? '))
L = int(input('How many years civilizations last? '))

num_detectable_civ = R * p * n * f * i * c * L


print('Base in the values entered...')
print('there are an estimated ', round(num_detectable_civ), 'potentially detectable civilizations in your galaxy')
