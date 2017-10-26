credits = int(input('Input earned credits: '))

if ( credits > 90 ):
    print('Senior status')
elif(credits > 60):
    print('Junior Status')
elif( credits > 30 ):
    print('Sophmore Status')
else:
    print('Freshman Status')
