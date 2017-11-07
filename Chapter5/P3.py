def modCount(n, m):
    if(m <= n):
        inBetween  = n - m
        dividible = []
        for x in range(m+1, n):
            if(x%m == 0):
                dividible.append(x)

        return 'There are  {} numbers between {} and  {} \nand the ones that are dividible by {} are {}'.format(inBetween, m, n, m, dividible)
    else:
        return 'n must be higher value then m'


print(modCount(10,2))
