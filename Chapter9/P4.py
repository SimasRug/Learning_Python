def getWeekAvgTemp(temp):
    week_avg = 0

    for x in temp:
        week_avg = week_avg + temp[x]
    
    week_avg = week_avg / len(temp)

    return round(week_avg, 2)


t = {'Monday': 80, 'Teusday':75, 'Wenesday':79, 'Thursday':50,'Firday':70, 'Saturday':89, 'Sunday':100}
print(getWeekAvgTemp(t))