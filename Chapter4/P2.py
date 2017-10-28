array = []
array1 =[]
tuple_valid = (3,5,18)


length = int(input('How many values do you want to enter?: '))

for x in range(0, length):
    print('Enter ', x+1 ,'number: ', end=' ')
    data = int(input())
    array1.append(data)
    if(data in tuple_valid):
        array.append(data)

print(array1)
print(array)
