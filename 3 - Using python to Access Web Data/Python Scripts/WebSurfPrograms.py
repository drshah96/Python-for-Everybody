### Retrieving Web Page Using URLLIB in Python

import urllib.request

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

###Counting Words
import urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)

### Parsing Web Pages
import urllib.error
from bs4 import BeautifulSoup

url = input('Enter URL: ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

### Parsing Web Pages by ignoring SSL Certificatrd
import urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL Certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
print(tags)
for tag in tags:
    print(tag.get('href', None))

### Quiz
# 1
x = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')  # File Handle

# 2
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)
while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()

import re

tags = '<p>Please click <a href="http://www.dr-chuck.com">here</a></p>'
y = re.findall('(.+)', tags)
print(y)
# http://www.dr-chuck.com

### Graded Assignment 1
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_445369.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
count = 0
b = list()
sum = 0
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    # print('TAG:', tag)
    # print('URL:', tag.get('href', None))
    # print('Contents:', tag.contents[0])
    # print('Attrs:', tag.attrs)
    # type(tag.contents)
    # sum = sum + tag.contents[0]
    # b.append(tag.contents[0])
    b.append(tag.contents[0])
    count = count + 1
print(count)
print(b)
b = list(map(int, b))
print(b)
for element in b:
    sum = sum + element
print(sum)

### Graded Assignment 2
import urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/known_by_Marin.html"
postion = int(input("Enter Position: "))
count = int(input("Enter Count: "))
count = count + 1

while (int(count) != 0):
    print("Retrieving: ", url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    pos = 1

    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        if (pos == int(postion)):
            # print("Retrieving: " ,pos, tag.get('href', None))
            url = tag.get('href', None)
            break
        # print(pos, tag.get('href', None))
        pos = pos + 1

    count = count - 1
