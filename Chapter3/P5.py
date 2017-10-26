positive = 0;
negative = 0;

while True:
    number = int(input('Enter number: '))
    if(number>=0):
        positive = positive + 1
    else:
        negative = negative + 1

    print('positive numbers: ', positive, ' Negative numbers: ', negative)
