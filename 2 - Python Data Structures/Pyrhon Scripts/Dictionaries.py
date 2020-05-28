# Making Dictionary
purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissue'] = 75
print(purse)

print(purse['candy'])
purse['candy'] = purse['candy'] + 2
print(purse)

# Dictionary Constants
jjj = {'chuck': 1, 'fred': 42, 'jan': 100}
print(jjj)

# Empty Dictionary
a = {}

# Manual Counters with Dictionary
ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)

ccc['cwen'] = ccc['cwen'] + 1
print(ccc)

# Automatic Counters with Dictionary
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)

# Get Method
if name in counts:
    x = counts[name]
else:
    x = 0
x = counts.get(name, 0)

# Counting using get()
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)

# Counting Pattern
counts = dict()
print('Enter a line of text:')
line = input('')
words = line.split()
print('Words: ', words)
print('Counting...')
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts', counts)

# Definite Loops and dictionaries
counts = {'chuck': 1, 'fred': 42, 'jan': 100}
for key in counts:
    print(key, counts[key])
print('BLASTOFF!!')

# Retriving list of Keys and Values
print(counts.keys())
print(counts.values())
print(counts.items())

# Two iteration Variables
jjj = {'chuck': 1, 'fred': 42, 'jan': 100}
for key, value in jjj.items():
    print(key, value)
print('BLASTOFF!!')

# Determining Max count and Word using Two Loops
name = input('Enter File:')
source = "/Users/dhruvinshah96/Documents/Programming Practice/Python/Coursera/Python for Everybody/2 - Python Data Structures/Pyrhon Scripts/Data/"
fname = source + name
handle = open(fname)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[words] = counts.get(word, 0) + 1
print("Done!")

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)

##### Graded Assignment 1 #####
name = input("Enter file:")
counts = dict()

try:
    if len(name) < 1:
        name = "mbox-short.txt"
    handle = open(name)

except:
    print('File cannot Opened: ', name)
    quit()

for line in handle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    email = words[1]
    # print(email)
    counts[email] = counts.get(email, 0) + 1
    # print(counts.items())

maxcount = None
maxword = None

for email, count in counts.items():
    if maxcount is None or count > maxcount:
        maxcount = count
        maxword = email
print(maxword, maxcount)
