import datetime

zodiac_animals = ('Rat', ['Ox', 'Watter Buffalo'], 'Tiger', ['Rabbit', 'Cat'], 'Dragon', 'Snake', 'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', ['Pig', 'Wild Boar'])

rat = 'Fortright, indusrius, sensitive, intelectual, sociable'
ox = 'Dependable, methodical, modest, born leader, patient'
tiger = 'Upredictable, rebellious, passionate, daring impulsive'
rabbit = 'Good friend, kind, soft-spoken, cautius, artistic'
dragon = 'Strong, self-assured, proud, decisive, loyal'
snake = 'Deep thinker, creative, responsible, calm, purposeful'
horse = 'Cheerful, quick-witted, perceptive, talkative, open-minded'
goat = 'Sincere, symphathetic, shy, generous, mothering'
monkey = 'Motivator, inquisitive, flexible, innovative, problem solver'
rooster ='Organized, self-assured, decisive, perfectionist, zaelous'
dog = 'Honest, unpretentious, idealistic, moralistic, easy going'
pig = 'Peace-lovin, hard-working, trusting, understanding, thoughtful'

characteristics = (rat, ox, tiger, rabbit, dragon, snake, horse, goat, monkey, rooster, dog, pig)

terminate = False

print('This program will display your Chineese zodiac and characteristics \n')

current_yr = datetime.date.today().year

while not terminate:
    birth_yr = int(input('Enter your year of birth: '))
    calendar = input('What kind of calendar would you like to see Chineese/c, Japaniese/j, Vietnamiese/v: ')

    while calendar != 'c' and calendar !='j' and calendar !='v':
        calendar = input('What kind of calendar would you like to see Chineese/c, Japaniese/j, Vietnamiese/v: ')

    while birth_yr < 1900 or birth_yr > current_yr:
        print('Invalid year. Please re-enter: ')
        birth_yr = int(input('Enter your year of birth: '))

    cycle_num = (birth_yr - 1990) % 12

    if(cycle_num == 11 and calendar == 'j'):
        print('Your zodiac is ', zodiac_animals[cycle_num][1])
    elif((cycle_num == 1 or cycle_num == 3) and calendar == 'v'):
        print('Your zodiac is ', zodiac_animals[cycle_num][1])
    elif((cycle_num == 1 or cycle_num == 3 or cycle_num == 11) and calendar == 'c'):
        print('Your Chineese zodiac is ', zodiac_animals[cycle_num][0])
    else:
        print('Your Chineese zodiac is ', zodiac_animals[cycle_num])

    print('Your characteristics ', characteristics[cycle_num])

    response = input('Would you like to continue and input another year: y/n: ')
    while response !='y' and response !='n':
        response = input('Please enter y or n: ')

    if response == 'n':
        terminate = True
