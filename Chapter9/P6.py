def numVowels(value):
    vowels_set = set('aeiou')

    vowels = 0 
    consonants = 0

    value = set(value)

    for x in value:
        if x in vowels_set:
            vowels += 1
        else:
            consonants += 1

    return vowels, consonants


v, c = numVowels('This is a very long sentence')
print('The string has {} vowels and {} consonants'.format(v, c))