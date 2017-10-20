import datetime

month_birth = 11#int(input('Enter month born: '))
day_birth = 18#int(input('Enter day born: '))
year_birth = 1991#int(input('Enter year born: '))

current_month = datetime.date.today().month
current_day = datetime.date.today().day
current_year = datetime.date.today().year

num_sec_day = 24 * 60 * 60
numsec_year = 365 * num_sec_day

avg_num_sec_year = ((4*numsec_year) + num_sec_day) //4
avg_num_sec_month = avg_num_sec_year // 12

numsecs_1900_dob = (year_birth -1900 * avg_num_sec_year) + (month_birth - 1 * avg_num_sec_month) + (day_birth * num_sec_day)
numses_1900_today = (current_year - 1900 * avg_num_sec_year) + (current_month - 1 * avg_num_sec_month) + (current_day * num_sec_day)

age_in_secs = numses_1900_today - numsecs_1900_dob

print('You are appromximetly ', age_in_secs, ' seconds old')
