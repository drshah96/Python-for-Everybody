### Counting Email in Database

import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)
''')

fname = input('Enter File Name: ')
path = "Data/"

if (len(fname) < 1):
    fname = path + 'mbox-short.txt'

fhand = open(fname)
for line in fhand:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email = ?', (email,))
    row = cur.fetchone()

    if row is None:
        cur.execute('''
        INSERT INTO Counts (email, count) VALUES (?, 1)''', (email,))

    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))

    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()

### Graded Assignment 2
### Counting Email in Database

import sqlite3

conn = sqlite3.connect('Assignment2db.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)
''')

counts = dict()

try:

    name = "Data/mbox.txt"
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
    (emailname, org) = email.split("@")
    # print(email)
    # org = str(re.findall('@([^ ]*)', words[1]))
    counts[org] = counts.get(org, 0) + 1

sorted_dict = sorted(counts.items(), key=lambda x: x[1], reverse=True)

for org, count in sorted_dict:
    # print(org, count)
    cur.execute('''
        INSERT INTO Counts (org, count) VALUES (?, ?)''', (org, count))

    conn.commit()

sqlstr = 'SELECT org, count FROM Counts'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
