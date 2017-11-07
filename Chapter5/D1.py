import math


def convert_to_global(value, mes):
    value = float(value)
    if(mes == 'm'):
        return value
    elif(mes == 'mm'):
        return (value * 0.001)
    elif(mes ==  'cm'):
        return (value * 0.01)
    elif(mes ==  'km'):
        return (value * 1000)
    elif(mes ==  'in'):
        return (value * 0.0254)
    elif(mes ==  'ft'):
        return (value * 0.3048)
    elif(mes ==  'ya'):
        return (value * 0.9144)
    elif(mes ==  'ml'):
        return (value * 1609.34)



def to_other_values(value, mes):
    if(mes == 'm'):
        return value
    elif(mes == 'mm'):
        return (value * 1000)
    elif(mes ==  'cm'):
        return (value * 100)
    elif(mes ==  'km'):
        return (value * 0.001)
    elif(mes ==  'in'):
        return (value * 39.3701)
    elif(mes ==  'ft'):
        return (value * 3.28084)
    elif(mes ==  'ya'):
        return (value * 1.09361)
    elif(mes ==  'ml'):
        return (value * 0.000621371)





print('This program converts metric mesurments')

print_values = """
-----------------------
| milimiters  |   mm  |
| centimiters |   cm  |
| meters      |   m   |
| kilometers  |   km  |
-----------------------
| inches      |   in  |
| feet        |   ft  |
| yards       |   ya  |
| miles       |   ml  |
-----------------------
"""

print(print_values)

convert_from = input("Enter the value and messurment you want to convert from: ")
convert_value, convert_mes = convert_from.split()
convert_to = input("Enter the value and messurment you want to convert to: ")

meters = convert_to_global(convert_value, convert_mes)
final = to_other_values(meters, convert_to)
final = format(final, '.2f')

print('{} {} is {} {}'.format(convert_value, convert_mes, final, convert_to ))
