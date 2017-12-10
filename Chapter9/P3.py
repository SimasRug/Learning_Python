def getDailyTemps():
    t = {'Monday':'', 'Teusday':'', 'Wenesday':'', 'Thursday':'','Firday':'', 'Saturday':'', 'Sunday':''}
    for x in t:
        t[x] = int(input('Enter the temperature for {}: '.format(x)))
    return t

print(getDailyTemps())
