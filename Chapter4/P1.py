array = []
array1 = []

length = int(input('How many values do you want to put in?: '))

for x in range(0, length):
    print('Enter ', x+1 ,'number: ', end=' ')
    data = int(input())
    array1.append(data)
    if(1 <= data <=100):
        array.append(data)

print(array1)
print(array)
