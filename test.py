# class XYcoord(object):
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y

#     def __repr__(self):
#         return '(' + str(self.__x) + ',' \
#                    + str(self.__y) + ')'

    
#     def __add__(self, rCoord):
#         new_x = self.__x + rCoord.__x
#         new_y = self.__y + rCoord.__y

#         return XYcoord(new_x, new_y)



# coord = XYcoord(5,2)
# print(coord)


# coord_1 = XYcoord(4,2)
# coord_2 = XYcoord(6,10)

# coord_3 = coord_1 + coord_2

# print(coord_3)


def calc(num):
    dictionary = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    cond = False
    arr = []
        # print('test')
    arr.append(num//16)
    a = num % 16
    if a > 16:
        calc(a);
    else:
        arr.append(a)

    for x in range(0,len(arr)):
        if(arr[x] > 9 and arr[x] < 16):
            arr[x] = dictionary[arr[x]]
    
    return_val = ''.join(str(x) for x in arr)
    

    return return_val



num = 99
print(calc(num))



