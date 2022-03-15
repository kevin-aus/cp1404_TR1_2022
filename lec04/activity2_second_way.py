__author__ = 'Cue'

countries = ['China', 'India', 'United States', 'Indonesia', 'Pakistan']
populations = [1439323776, 1380004385, 331002651, 273523615, 220892340]
no_of_countries = len(countries)
first_letters = []

print('COUNTRIES')
print('=' * len('COUNTRIES'))
for i in range(0, no_of_countries):
    print(countries[i])
    first_letters.append(countries[i][0])
print(first_letters)
do_again = 'Y'
while do_again == 'Y':
    choice = input('Enter the first letter of a country: ').upper()

    try:
        print('Population of',
              countries[first_letters.index(choice)], 'is',
              populations[first_letters.index(choice)])
    except ValueError:
        print("{} is not a first letter of a country".format(choice))
    do_again = input('Enter y to continue or anything else to quit: ')
    do_again = do_again.upper()
print('Bye.')
