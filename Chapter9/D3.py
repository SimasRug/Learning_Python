def get_description():
    desc = input('Enter a descritpion for your entered value: ')
    return desc

def get_choice():
    choice = int(input('Enter 1 to add Hexodecimal and convert to Decimal or enter 2 to  add Decimal and convert to Hexodecimal: '))
    if (choice == 1 or choice == 2):
        return choice
    else:
        raise ValueError('Invalid input, try again')
 
def get_decimal():

    try:
        val = input('Enter the Hexodecimal number: #')
        if len(val) != 6:
            raise ValueError('Invalid input, try again')
        else:
            decimal = convert_to_base(val)
            description = get_description()
            val  = '#'+val
            return [description, decimal, val]


    except ValueError as err_msg:
        print(err_msg,'\n')
        get_decimal()

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




def get_hex():

    try:
        arr = ['','','']
        result_string = ''
        arr[0], arr[1], arr[2] = input('Enter a decimal number and separate it with a space: ').split()

        for x in arr:
            a = calc(int(x))
            result_string = result_string + str(a)

        description = get_description()

        decimal  = ' '.join(arr)
        return [description, decimal, result_string]
    
    except ValueError as err_msg:
        print(err_msg, '\n')
        get_decimal()


def convert_to_base(value):
    dictionary = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    value_array = list(value)
    return_arr = []
    for x in range(0 ,len(value_array)):
        if value_array[x] in dictionary:
            value_array[x] = dictionary[value_array[x]]
    

    for x in range(0, len(value_array),2):
        t = (int(value_array[x])*16) + int(value_array[x+1])
        return_arr.append(t)
        return_string = ' '.join(str(x) for x in return_arr)

    return return_string


# ----------------------------------------------------------------

valid_input = False
all_values = []

while not valid_input:
    try:
        choice = get_choice()
        valid_input = True

        if choice == 1:
            from_dec = get_decimal()
            all_values.append(from_dec)
        elif choice == 2:
            from_hex = get_hex()
            all_values.append(from_hex)


    except ValueError as err_msg:
        print(err_msg,'\n')


print(all_values)
