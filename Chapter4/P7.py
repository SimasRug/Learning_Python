array1 = []
array = []
same_values = []
total = 0
total1 = 0

length = int(input('How many values do you want to put in first list?: '))

#Make this into a function !!!
for x in range(0, length):
    print('Enter ', x+1 ,'number: ', end=' ')
    data = int(input())
    array.append(data)
    total = total + data


length = int(input('How many values do you want to put in second list?: '))

for x in range(0, length):
    print('Enter ', x+1 ,'number: ', end=' ')
    data = int(input())
    array1.append(data)
    total1 = total1 + data


for x in array:
    if(x in array1):
        same_values.append(x)

print('/n')

if(len(array) == len(array1)):
    print('Lists are the same length')
else:
    print('Lists are not the same leght')

if(total1 == total):
    print('Lists sum values ar the same')
else:
    print('Lists sum values ar NOT the same')

if(len(same_values) > 0):
    print('Same values on both lists',same_values)
else:
    print('There are no recurring in both lists ')



print(array)
print(array1)
