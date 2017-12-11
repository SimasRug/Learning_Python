test_number = '2471A3'

def convert_to_base(value):
    dictionary = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    value_array = list(value)
    return_arr = []
    for x in range(0 ,len(value_array)):
        if value_array[x] in dictionary:
            value_array[x] = dictionary[value_array[x]]
    

    for x in range(0, len(value_array),2):
        print(value_array[x])
        t = (int(value_array[x])*16) + int(value_array[x+1])
        print(t)
        return_arr.append(t)


    # print(value_array[x])
    return return_arr



print(convert_to_base(test_number))