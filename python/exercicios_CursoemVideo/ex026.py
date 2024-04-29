
phrase = str(input('Type the phrase: ')).strip()
test = phrase.upper()

print('The number of A in phrase is {}'.format(test.count('A')))
print('The first ocurrence of A is {}'.format(test.find('A') + 1))
print('The last ocurrence of A is {}'.format(test.rfind('A') + 1))
