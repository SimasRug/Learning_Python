total = 0
temp = 1

for x in range(64):
    temp = temp * 2
    total = total + temp
    # print(x, temp, total);


total_weight = total/7000

print('total weight: ', total_weight)
