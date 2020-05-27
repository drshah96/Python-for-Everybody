###Combining two Strings
str1 = "Hello"
str2 = 'There'
bob = str1 + str2
print(bob)

# Combining by manipulating
str2 = str1 + 'There'
print(str2)

str = str1 + ' ' + 'There'

str3 = '123'
# str3 = str3 + 1 #Error
str3 = int(str3) + 1
print(str3)

# Reading from input
name = input('Enter Name: ')
print(name)

# Looking inside letter
fruit = 'banana'
letter = fruit[1]
print(letter)
print(len(fruit))

x = 3
w = fruit[x - 1]
print(w)

index = 0
# While Loop
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

# For Loop
for letter in fruit:
    print(letter)

# Counting letter a in banana
count = 0
for letter in fruit:
    if letter == 'a':
        count = count + 1
print("Count of letter a: ", count)

### Using 'in' as a Logical Operator
fruit = 'banana'
'n' in fruit

if 'a' in fruit:
    print('Found')

### String Comparison
word = 'Bana'
if word == 'banana':
    print('All right, bananas.')

if word < 'banana':
    print('Your word, ' + word + ', comes before banana.')

elif word > 'banana':
    print('Your word, ' + word + ', comes after banana.')

else:
    print('All right, bananas.')

### Sring Casing
greet = 'Hello'
print(greet.lower())
print('Hi There'.upper())

### Finding Type and Directory
type(greet)
dir(greet)

# Finding string or letter
fruit = 'banana'
pos = fruit.find('na')
print(pos)

pos = fruit.find('z')
print(pos)

### Replacing String
greet = "Hello Abc"
nstr = greet.replace('Hello', 'Hi')
print("Replacing Hello with Hi : ", nstr)

fruit = 'banana'
nstr = fruit.replace('n', 'z')
print(nstr)

### Stripping WhiteSpace
greet = '     Hello Abc  '
print(greet.lstrip())
greet.rstrip()
greet.strip()

### Prefixes
line = "please shut the door"
line.startswith('please')
line.startswith('p')

### Parsing and Extracting
data = 'From abc.xyz@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ', atpos)
print(sppos)

host = data[atpos + 1: sppos]
print(host)

##### QUIZ #####
x = 'From marquard@uct.ac.za'
print(x[8])
print(x[14:17])

for letter in 'banana':
    print(letter)

print(len('banana') * 7)

greet = 'Hello Bob'
print(greet.upper())

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos + 3])

##### Practice Assignent #####
text = "X-DSPAM-Confidence:    0.8475";

a = text.find('0.8475')
b = text[a:29]

print(float(b))
