def getData():
    term = input('Enter two values number values to get their ratio ex.:"50 100": ')
    return extractValues(term)


def extractValues(value):
    tup = value.strip(' ').split(' ')
    tup = tuple(tup)
    return calcRatios(tup)

def calcRatios(numbers):

    return float(numbers[0]) / float(numbers[1])




print(getData())