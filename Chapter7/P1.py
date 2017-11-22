def convertStatus(letter):
    """This program return a word for a defined letter"""
    letters = {'f':'freshman','s':'sophomore','j':'junior','r':'senior'}

    if(letter in letters):
        return letters[letter]
    else:
        return 'Error'


user = input('Input a letter so you could get a word back: ')
print(convertStatus(user))