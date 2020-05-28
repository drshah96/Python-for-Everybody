# List Constants
print([1, 24, 76])
print([1, [5, 6], 7, 'red'])

# List in Loop
for i in [5, 4, 3, 2, 1]:
    print(i)
print('Blastoff!')

# Lists and Definite Loops
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')

# Looking Inside List
print(friends[1])

# Lists are Mutable
lotto = [2, 14, 26, 41, 63]
print(lotto)
lotto[2] = 28
print(lotto)

# Range Function
print(range(4))
print(len(friends))
print(range(len(friends)))

# A Tale of Two Loops
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)

for i in range(len(friends)):
    friend = friends[i]
    print('Happy New Year:', friend)

# Concating Lists
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
print(a)

# Slicing Lists
t = [9, 41, 12, 3, 74, 15]
print(t[1: 3])
print(t[:4])
print(t[3:])
print(t[:])

# Lists Methods
x = list()
print(type(x))
print(dir(x))

# Building List from Scratch
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)
stuff.append('cookie')
print(stuff)

# Checking element in List
some = [1, 9, 21, 10, 16]
print(9 in some)
print(15 in some)

# Lists are in order
friends = ['Joseph', 'Glenn', 'Sally']
friends.sort()
print(friends)

# Built-in Functions and Lists
nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums) / len(nums))

numlist = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average: ', average)

# Strings and Lists
abc = "With three words"
stuff = abc.split()
print(stuff)
print(stuff)

for w in stuff:
    print(w)

#
line = "A Lot"
etc = line.split()
print(etc)

line = 'first;second;third'
thing = line.split()
print(thing)
print(len(thing))

thing = line.split(';')
print(thing)
print(len(thing))

# Extracing from line
line = 'From abc.xyz@uct.ac.za Sat Jan  5 09:14:16 2008'
words = line.split()
print(words)
email = words[1]
print(email)
pieces = email.split('@')
print(pieces[1])

##### QUIZ #####
friends = ['Joseph', 'Glenn', 'Sally']
print(friends[2])

fruit = 'Banana'
# fruit[0] = 'b'
print(fruit)

x = list(range(5))
print(x)
print(type(x))

t = [9, 41, 12, 3, 74, 15]
print(t[2:4])

friends = ['Joseph', 'Glenn', 'Sally']
friends.sort()
print(friends[0])

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(len(c))

##### Graded Assignment 1 #####
fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    line = line.rstrip()
    word = line.split()
    # print(word)
    lst.append(word)

a = lst[0] + lst[1] + lst[2] + lst[3]
a.sort()

b = list()

for i in a:
    # word = a[i]
    # print(i)
    if not i in b:
        b.append(i)

print(b)

##### Graded Assignment 2 #####

fname = input("Enter file name: ")
if len(fname) < 1: fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    email = words[1]
    print(email)
    count = count + 1

print("There were", count, "lines in the file with From as the first word")
