def peek(stack):
    for x in stack:
        print('-----')
        print('| {} |'.format(x))
        print('-----')





def  getString(val):
    val = val.split(' ')
    print(val)
    val = list(filter(lambda x: x != '' , val))
    print(val)
    stack = []
    result = a(val, stack)
    return str(result)





def a(val, stack):

    if len(val) == 0:
        return stack[0]
    else:
        if val[0] in '+-*/':
            if val[0] == '+':
                stack[0] = stack[1] + stack[0]
            elif val[0] == '-':
                stack[0] = stack[1] - stack[0]
            elif val[0] == '*':
                stack[0] = stack[1] * stack[0]
            elif val[0] == '/':
                stack[0] = stack[1] / stack[0]
            
            del stack[1]
            del val[0]
            return a(val, stack)
     
        else:
            stack.insert(0, int(val[0]))
            del val[0]
            return a(val, stack)



print(getString('31 42 3 * -'))