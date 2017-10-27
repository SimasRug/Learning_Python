loan_amount = 350000 #int(input('Enter loan amount: '))
term = 30#int(input('enter term leght in years: '))


print('Loan amount: $',loan_amount, ' Term:', term,'years')
n = term*12


print('Interest Rate  Monthly Payment')
for x in range(3,19):
    r = (x/100.0)/12
    D = ( ((1+r)**n) - 1 ) / (r * (1+r)**n)
    print(format('','>8'), x,'%', format(' ','>2'), format(loan_amount/D, '.2f'))
