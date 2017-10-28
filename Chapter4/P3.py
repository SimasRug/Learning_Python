array = []


length = int(input('How many values do you want to enter?: '))

for x in range(0, length):
    print('Enter ', x+1 ,'number: ', end=' ')
    data = int(input())
    if(data > 100):
        array.append('over')
    else:
        array.append(data)

print(array)
