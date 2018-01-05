class Money(object):
    def __init__(self, dollars, cents):
        self.__dollars = dollars
        self.__cents = cents
        self.__all = self.__dollars + (self.__cents/100)

    def __add__(self, other):
        return '$ %.2f' % (self.__all + other.__all)

    def __repr__(self):
        return '$ %.2f' % (self.__all)

    def convertToEuro(self):
        return '$ %.2f' % (self.__all * 0.84)

    def convertToGDP(self):
        return '$ %.2f' % (self.__all * 0.74)

    def convertToYen(self):
        return '$ %.2f' % (self.__all * 112.51)


   


t = Money(1,60)
print(t)
a = Money(5,10)
print(a)
print(t+a)

b = Money.convertToYen(t)
print(b)