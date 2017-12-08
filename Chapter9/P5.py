def addVegetable(value):
    add = input('Add a vegetable to the existing set: ')
    if add not in value:
        value.add(add)
    return value


t = set(['apple', 'banana', 'peach'])
t = addVegetable(t)
print(t)