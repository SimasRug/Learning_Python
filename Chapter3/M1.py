print('This program will convert temperature (F/C)')
print('Enter temperature to convert C to F')
print('Enter temperature to convert F to C')
print('Enter temperature to convert K to C')

which = input('Enter selection: ')

while which !='F' and which != 'C' and which !='K':
    which = input('Please enter C or F or K: ')

temp = int(input('Input temperature to convert: '))


if which == 'F':
    while temp <= -459.67:
        temp = int(input('Please neter valid number for F '))
    converted_temp = format((temp - 32) * 5/9, '.1f')
    print(temp,' F converted to C is equal ', converted_temp)
elif which == 'C':
    while temp <= -273.15:
        temp = int(input('Please neter valid number for C '))
    converted_temp = format((9/5 * temp) +32 , '.1f')
    print(temp,' C converted to F is equal ', converted_temp)
elif which == 'K':
    converted_temp = format(temp + 273.15, '.1f')
    print(temp,' K converted to C is equal ', converted_temp)
