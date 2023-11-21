# Characters in a string
fruit = 'banana'
letter = fruit[0]
print(letter)

x = 3
w = fruit[x + 2]
print(w)

# Looping through strings

# While loop
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index +=1

# For loop
fruit = 'watermelon'
for letter in fruit:
    print(letter)

# String looping and counting
word = 'banana' 
count = 0
for letter in word:
    if letter == 'a':
        count += 1
print(count)

# Slicing Strings
name = 'Cleomark Ian'
print(name[0:4])
print(name[9:12]) 

# String Concatenation
name = 'Cleo'
greet = 'Hey' + ' ' + name
print(greet)

# Using 'in' as a logical operator
name = 'cleo'
if 'e' in name:
    print('positive')

# String Comparison
name = 'cleo'
if name == 'cleo':
    print('equal')

if name < 'cleo':
    print(name + ' ' + 'comes before cleo')
elif name > 'cleo':
    print(name + ' ' + 'comes after cleo')
else:
    print('same')

# String Library

# To lower case
greet = 'Hey Cleo'
zap = greet.lower()
print(zap)
print('yOU GoOd?'.lower())

# Finding a substring
name = 'cleomark'
position = name.find('mark')
print(position)
print(name.find('i'))

# Searching and replacing a substring
greet = 'Hello Cleo'
print(greet.replace('Cleo', 'Ian'))
print(greet.replace('o', 'm'))

# Stripping Whitespace
greet = '   Hello Cleo   '
print(greet.strip())
print(greet.lstrip()) #left strip
print(greet.rstrip()) #right strip

# Prefixes
greet = 'Hey cleo'
print(greet.startswith('Hey'))
print(greet.startswith('hey'))

# Parsing and Extracting
data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
startpos = data.find('@')
endpos = data.find(' ', startpos)
print(data[startpos+1 : endpos])
