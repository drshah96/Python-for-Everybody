# Comparing re.search() Like find()
# re.search() returns True or False
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.find('From:') >= 0:
        print(line)

import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)

# Comparing re.search() Like startswith()
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.startswith('From:') >= 0:
        print(line)

import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)

# Wild Card Characters
import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^X.*:', line):
        # Starting with X followed by any-character(.) for any number of times(*) till ':'
        print(line)
    if re.search('^X-\S+:', line):
        # Starting with 'X-' then Match non-whitespace character '\S' then one or more times '+' till ':'
        print(line)
print("Done")

# Matching and Extracting Data
import re

# re.findall() extracts Match Strings
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x)  # One or More Digits
print(y)

y = re.findall('[AEIOU]+', x)  # UpperCase Values
print(y)

# Greedy Matching (* and +)
import re

x = 'From: Using the : character'
y = re.findall('^F.+:', x)  # First Character 'F' then one or More Characters '+' Last character ':'
print(y)
# Non-Greedy (?)
y = re.findall('^F.+?:', x)  # First Character 'F' till first ':'
print(y)

# Fine - Tunning String Extraction
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+@\S+', x)  # At least one non-whitespace character '\s'
print(y)

y = re.findall('^From (\S+@\S+)',
               x)  # Starts from From At least one non-whitespace character '\s' and Parenthesis indicates Start and Stop of Match
print(y)

# The Double Split Pattern
line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
words = line.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])

y = re.findall('@([^ ]*)',
               line)  # Start from @, Extract from parenthesis, '[^ ] Match non-blank characters, '*' Match many of them
print(y)

print(line)
y = re.findall('^From .@([^ ]*)', line)
print(y)

# Spam Confidence
import re

hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1: continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))

# Escape Character
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+', x)
print(y)

##### QUIZ #####
line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('@(\S+)', line)
print(y)

x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)

##### Graded Assignment #####
## Extracting numbers from Text File and Summing up ##
import re

source1 = '/Users/dhruvinshah96/Documents/Programming Practice/Python/Coursera/Python for Everybody/3 - Using python to Access Web Data/Python Scripts/Data/regex_sum_42.txt'
file = '/Users/dhruvinshah96/Documents/Programming Practice/Python/Coursera/Python for Everybody/3 - Using python to Access Web Data/Python Scripts/Data/regex_sum_445367.txt'

try:
    handle = open(file)
    print('File Loaded')

except:
    print('File cannot Opened')
    quit()

count = 0
numlist = list()
for line in handle:
    line = line.rstrip()
    # print(line)
    number = re.findall('[0-9]+', line)
    print(number)
    if len(number) != 0:
        for i in number:
            count = count + 1
            num = int(i)
            numlist.append(num)

print(numlist)
print('Number of Values: ', count)
print("Sum: ", sum(numlist))
