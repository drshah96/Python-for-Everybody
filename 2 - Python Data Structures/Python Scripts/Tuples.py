# Tuples are Like Lists
x = ('Glenn', 'Sally', 'Joseph')
print(x[2])

y = (1, 9, 2)
print(y)
print(max(y))

for iter in y:
    print(iter)

# Tuples are not mutable but list are
x = [9, 8, 7]
x[2] = 6
print(x)

# Tuples cannot be append, sort or reverse
t = tuple()
print(dir(t))

# Tuples and Assignment
(x, y) = (4, 'fred')
print(y)

(a, b) = (99, 98)
print(a)

# Tuples and Dictionaries
d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k, v) in d.items():
    print(k, v)
tups = d.items()
print(tups)

# Tuples are Comparable
print((0, 1, 2) < (5, 1, 2))

# Sorting List of Tuples
d = {'a': 10, 'b': 1, 'c': 22}
print(d.items())
print(sorted(d.items()))

# Using sorted()
d = {'a': 10, 'b': 1, 'c': 22}
t = sorted(d.items())
t

for k, v in sorted(d.items()):
    print(k, v)

# Sort by values
c = {'a': 10, 'b': 1, 'c': 22}
tmp = list()
for k, v in c.items():
    tmp.append((v, k))
print(tmp)

tmp = sorted(tmp, reverse=True)
print(tmp)

# Ten Most Common Words
fhand = open('')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for val, key in lst[: 10]:
    print(key, val)

# List Comprehension: Shorter Version
c = {'a': 10, 'b': 1, 'c': 22}
print(sorted([(v, k) for k, v in c.items()]))
print(sorted([(v, k) for k, v in c.items()], reverse=True))

##### QUIZ #####
x, y = 3, 4

x = {'chuck': 1, 'fred': 42, 'jan': 100}
y = x.items()
print(y)

x = (5, 1, 3)
if (6, 0, 0) > x:
    print(True)

tmp = list()
for k, v in c.items():
    tmp.append((v, k))

days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print(days[2])

##### Graded Assignent 1 #####
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
    time = words[5]
    time = time.split(":")
    time = time[0]
    counts[time] = counts.get(time, 0) + 1

t = sorted(counts.items())

for key, val in t:
    print(key, val)
