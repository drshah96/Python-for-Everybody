# Sockets
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
mysock.close()

# An HTTP Request in fetching File Python
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

count = 0
text = b""

while True:
    data = mysock.recv(512)
    if (len(data) < 1): break
    print(data.decode())
    text = text + data
mysock.close()

pos = text.find(b"\r\n\r\n")
print('Header Length: ', pos)
print(text[:pos].decode())

text = text[pos + 4:]
path = '/Users/dhruvinshah96/Documents/Programming Practice/Python/Coursera/Python for Everybody/3 - Using python to Access Web Data/Output/'
fname = path + 'OutputFile.txt'
fhand = open(fname, "wb")
fhand.write(text)
fhand.close()

# Retriving an image over HTTP
import socket

HOST = 'data.pr4e.org'
PORT = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))

cmd = 'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n'.encode()
mysock.sendall(cmd)
count = 0
picture = b""

while True:
    data = mysock.recv(5120)
    if len(data) < 1: break
    count = count + len(data)
    print(len(data), count)
    picture = picture + data

mysock.close()

pos = picture.find(b"\r\n\r\n")
print('Header Length: ', pos)
print(picture[:pos].decode())

picture = picture[pos + 4:]
path = '/Users/dhruvinshah96/Documents/Programming Practice/Python/Coursera/Python for Everybody/3 - Using python to Access Web Data/Output/'
fname = path + 'OutputImage.jpg'
fhand = open(fname, "wb")
fhand.write(picture)
fhand.close()
