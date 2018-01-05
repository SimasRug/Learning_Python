class FootMeasure(object):
    def __init__(self, feet = 0, inches = 0):
        self.__feet = feet
        self.__inches = inches


    def __repr__(self):
        if(self.__inches == 0):
            return '%s ft. %s in.' % (self.__feet, self.__inches)
        else:
          return '%s in.' % (self.feetToinches())  

    def __add__(self, other):
        test = self.feetToinches() + other.feetToinches()
        return '%s in.' % (test)

    def feetToinches(self):
        return (self.__feet*12) + self.__inches
        




t = FootMeasure(15, 1)
a = FootMeasure(15, 1)

# t.test()
c = t+a
print(c)