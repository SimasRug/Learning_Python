
array = []

length = int(input('How many values do you want to enter?: '))

for x in range(0, length):
    print('Enter ', x+1 ,'name: ', end=' ')
    fruit = input()
    print('Enter its weight: ', end=' ')
    weight = int(input())
    temparr = [fruit, weight]
    array.append(temparr)

array.sort()
print(array)
