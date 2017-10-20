num_atoms_universe = 10e80
weight_avg_person = 70
num_atoms_avg_person = 7e27

print('This program will determine your place in the universe')

weight_kg = int(input('Input your weight in kg: '))

num_atoms = (weight_kg/70)*num_atoms_avg_person
percent_of_universe =(num_atoms / num_atoms_universe)*100

print('You contain appromximetly', format(num_atoms, '.2e') , 'atoms')
print('Therefore, you comprise', format(percent_of_universe, '.2e'), '% of the universe')
