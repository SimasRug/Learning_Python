array = []

length = int(input('How many values do you want to enter?: '))

for x in range(0, length):
    print('Enter ', x+1 ,'name: ', end=' ')
    data = input()
    if( data.count(data[0]) > 1):
        array.append(data)

print(array)
