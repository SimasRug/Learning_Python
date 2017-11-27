test = '(this is (test (for parentheses) it should) work)'
# test = 'this a false string'


def matchPar(string):
    open_par = string.count('(')
    closed_par = string.count(')')
    if( open_par == closed_par):
        if(open_par != 0 and closed_par != 0):
            return 'Parantheses DO match' 
        else:
            return 'No parantheses at all'
            
    else:
         return 'The parantheses dont match'


print(matchPar(test))