test_number = 'FF6347'

def convert_to_base(value):
    dictionary = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    value_array = list(value)
    for x in range(0, len(value_array),2):
        if value_array[x] in dictionary:
            x = dictionary[value_array[x]]
            print(x)
        print(value_array[x])
    return value_array



print(convert_to_base(test_number))