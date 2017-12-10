import copy
def moderateDays(value):
    arr = []
    for x in value:
        if value[x] > 69 and value[x] < 80:
            arr.append(x)
    return arr

t = {'Monday': 80, 'Teusday':75, 'Wenesday':79, 'Thursday':50,'Firday':70, 'Saturday':89, 'Sunday':100}
print(moderateDays(t))



