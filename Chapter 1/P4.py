first = int(input('Enter leftmost digit: '))
second = int(input('Enter next digit: '))
third = int(input('Enter next digit: '))
fourth = int(input('Enter next digit: '))

baseTen = (first*(2**3))+(second*(2**2))+(third*(2**1))+(fourth*(2**0))

print('The Value is', baseTen)
