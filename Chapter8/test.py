# empty_str = ''
# file_name = 'C:/Users/Rugeviciuss/Desktop/Python/Learning_Python/Chapter8/test.txt'
# file_name_copy = 'C:/Users/Rugeviciuss/Desktop/Python/Learning_Python/Chapter8/test_copy.txt'
# input_file = open(file_name,'r')
# output_file = open(file_name_copy,'w')

# line = input_file.readline()
# output_file.write(line)

# output_file.close()


import math 
# num = int(input('Enter number to compute factorial:'))
# valid_input = False

# while not valid_input:
#     try:
#         result = math.factorial(num)
#         print(result)
#         valid_input = True
#     except ValueError:
#         print('Cant comupte nagevtive numbers')
#         num = int(input('Please re-enter:'))


def getMonth():
    month = int(input('Enter current month (1-12): '))
    if month < 1 or month > 12:
        raise ValueError ('Invalid Month value')
    return month


valid = False

while not valid:
    try:
        month = getMonth()
        valid = True
    except ValueError as err_msg:
        print(err_msg,'\n')