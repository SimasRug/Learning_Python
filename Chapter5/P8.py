def func(array, trush):
    for x in range(0, len(array)):
        if(array[x]>5):
            array[x] = 0
    return array


a = [6,2,3,18,5,6]
b = func(a, 5)

print(b)
