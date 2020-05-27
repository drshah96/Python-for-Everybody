# File Handling as Sequence
xfile = open('abc.txt')
for cheese in xfile:
    print(cheese)

# Counting Lines in file
count = 0
for line in xfile:
    count = count + 1
print('Line Count: ', count)

# Reading Whole File
xfile = open('abc.txt')
inp = xfile.read()
print(len(inp))

print(inp[:20])

# Searching Through File
fhand = open("abc.txt")
for line in fhand:
    if line.startswith('From:'):
        print(line)
print("End")

fhand = open("abc.txt")
for line in fhand:
    line = line.rstrip()  # to extra avoid new lines
    if line.startswith('From:'):
        print(line)
print("End")

# Skipping with Continue
hand = open("abc.txt")
for line in fhand:
    line = line.rstrip()  # to extra avoid new lines
    if not line.startswith('From:'):
        continue
    print(line)
print("End")

# Using "in" in Select Lines
hand = open("abc.txt")
for line in fhand:
    line = line.rstrip()  # to avoid new lines
    if not '@uct.ac.za' in line:
        continue
    print(line)
print("End")

# User Input File Name
fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject: '):
        count = count + 1
    print('There were', count, 'subject lines in', fname)

# Bad File Names
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot opened: ', fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('Subject: '):
        count = count + 1
    print('There were', count, 'subject lines in', fname)

##### Graded Assignent 1 #####
# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line = line.rstrip()
    print(line.upper())

##### Graded Assignent 2 #####
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
add = 0.0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"): continue
    # print(line)
    add = add + float(line[20:26])
    count = count + 1
Average = add / count
print("Average spam confidence:", Average)
