array = []
total = 0


length = int(input('How many values do you want to enter?: '))

for x in range(0, length):
    print('Enter ', x+1 ,'name: ', end=' ')
    data = input()
    total = total + data.count('a')
    array.append(data)

print(array)
print('a acours', total, 'times')
