def palindromeChecker(word):
    """This function checks if the given word is polindrome and returns a boolean """

    if(word == word[::-1]):
        return True
    else:
        return False





word = input('Input a word and see if it is palindrome: ')

if(palindromeChecker(word)):
    print('{} is palindrome'.format(word))
else:
    print('{} is NOT palindrome'.format(word))