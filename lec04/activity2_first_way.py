__author__ = 'Cue'

countries = ['China', 'India', 'United States', 'Indonesia', 'Pakistan']
populations = [1439323776, 1380004385, 331002651, 273523615, 220892340]
no_of_countries = len(countries)
# for i in range(0, no_of_countries):
#    print('Population of',countries[i],'is',populations[i])

print('COUNTRIES')
print('=' * len('COUNTRIES'))
for i in range(0, no_of_countries):
    print(str(i+1)+'.',countries[i])

do_again = 'Y'
while do_again == 'Y':
    choice = int(input('Enter a number from 1 to 5: '))
    print('Population of',countries[choice-1],'is',populations[choice-1])
    do_again = input('Enter y to continue or anything else to quit: ')
    do_again = do_again.upper()
print('Bye.')