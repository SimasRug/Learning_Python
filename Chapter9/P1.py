import random
import copy
def addDailyTemp(value):
    new_value = copy.deepcopy(value)
    for x in new_value:
        if new_value[x] == '':
            new_value[x] = random.randrange(0,20)
    return new_value





test = {'Monday':'', 'Teusday':'', 'Wenesday':'', 'Thursday':'','Firday':'', 'Saturday':'', 'Sunday':''}
print(addDailyTemp(test))


