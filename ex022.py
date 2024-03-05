
name = input('Type a name: ')

# All upper letters
print(name.upper())
# All lower letters
print(name.lower())
# All words with upper initial letter
print(name.title())

withoutSpaces = name.replace(' ','')
print(len(withoutSpaces))
print(len(name) - name.count(' '))

firstName = name.split()
print(len(firstName[0]))
