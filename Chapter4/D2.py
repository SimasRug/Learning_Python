import datetime

days = [[11, 31, 'New years Eve'], [2, 14, 'Valentines day'], [3, 17, 'St. Patricks Day'], [4, 1, 'April Fools Day'], [7, 4, 'Fourth of July'],  [5, 1, 'Labor Day'], [10, 31, 'Halloween']]
year = int(input('Input the year: '))
# birth_month = int(input('Input your birth month: '))
# birth_day = int(input('Input your birth day: '))
# days.append([birth_month, birth_month, 'Your birthday'])

week_days = { 1: 'Monday', 2: 'Teusday', 3: 'Wenesday', 4:'Thursday', 5:'Friday', 6:'Saturday', 7:'Sunday'}



a = datetime.datetime(year, days[0][0], 23, 0, 0, 0, 0).weekday()
print(a)
# print('In the year', year)
for x in days:
    weekday = datetime.datetime(year, x[0], x[1], 0, 0, 0, 0).weekday()
    # print(x[2], 'was ', week_days[weekday] )

# print(datetime.datetime.today().weekday())
