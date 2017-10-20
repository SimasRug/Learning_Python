tax = float(input('Enter restaurant tax: '))

print('This program will calculate a restaurant tab for a couple with')
print('a gift certificate, with a restaurant tax of', tax*100,'% \n' )

amt_certificate = float(input('Enter amount of the gift certificate: '))

print('Enter ordered items for person 1')

appetizer_per1 = float(input('Appetizer: '))
entree_per1 = float(input('Entree: '))
drinks_per1 = float(input('Drinks: '))
dessert_per1 = float(input('Dessert:'))


print('Enter ordered items for person 2')

appetizer_per2 = float(input('Appetizer: '))
entree_per2 = float(input('Entree: '))
drinks_per2 = float(input('Drinks: '))
dessert_per2 = float(input('Dessert:'))


amt_person1 = appetizer_per1 + entree_per1 + drinks_per1 + dessert_per1
amt_person2 = appetizer_per2 + entree_per2 + drinks_per2 + dessert_per2

drink_cost = drinks_per1 + drinks_per2

desert_cost = dessert_per1 + dessert_per2

items_cost = amt_person1 + amt_person2

tab = items_cost + items_cost * tax

print('\nOrdered items: $', format(items_cost, '.2f'))
print('\nOrdered drinks: $', format(drink_cost, '.2f'))
print('Ordered desert: $', format(desert_cost, '.2f'))
print('\nTab: $', format(tab - amt_certificate, '.2f'))
print('Negative anount indicates unused amount of gift certificate')
