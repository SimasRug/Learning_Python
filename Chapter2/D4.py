def return_average(a, b, range_size):
    count = 0
    for x in range (a,b):
        count = x + count
    return (count/range_size)*525600

def return_breath_avg(user_age):
    lived_seconds = user_age*31557600
    return 67.5 * lived_seconds

infant_avg = return_average(30,61,30)
baby_avg = return_average(20,31,10)
kid_avg = return_average(15,26, 10)
adult_avg = return_average(12,21,8)
total_count = 0

# print(infant_avg)

user_age = int(input('Enter your age: '))

for x in range(0, user_age+1):
    if x <= 1:
        total_count = total_count + infant_avg
    elif 2 <= x <= 4 :
        total_count = total_count + baby_avg
    elif 5 <= x <= 14:
        total_count = total_count + kid_avg
    elif 15 <= x:
        total_count = total_count + adult_avg


user_breaths = return_breath_avg(user_age)

print("The total heart beats you had in your lifetime is: ", total_count, ' and you had ', user_breaths ,' breaths')
