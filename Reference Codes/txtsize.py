import os

for (dirname, dirs, files) in os.walk('.'):
    for filename in files:
        if filename.endswith('.txt'):
            thefile = os.path.join(dirname, filename)
            print(os.path.getsize(thefile), thefile)
