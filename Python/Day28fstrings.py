letter = 'Hey my name is {} and I am from {}'
country = "Nepal"
Name = "Nikhil Sah"
print(letter.format(Name,country))


letter = 'Hey my name is {1} and I am from {0}'
country = "Nepal"
Name = "Nikhil Sah"
print(letter.format(country,Name))


letter = 'Hey my name is {} and I am from {}'
country = "Nepal"
Name = "Nikhil Sah"
print(f'Hey my name is {Name} and I am from {country}')
print(f'Hey my name is {{Name}} and I am from {{country}}')


price = 21.22231
txt = f"for only {price:.2f} dollars"
print(txt)


txt = "for only {price:.2f} dollars"
print(txt.format(price=49.099999))


a = print(f'{3*4}')
print(type(a))
print(type(f'{3*4}'))


