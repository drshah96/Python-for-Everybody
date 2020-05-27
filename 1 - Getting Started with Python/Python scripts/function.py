#Basic Function
def thing():
    print('Hello')
    print('Fun')

thing()
print('Zip')
thing()

#Random Function Program
x = 5
print('Hello')

def print_lyrics():
    print("I'm a lumberjack, and I'm okay")
    print('i sleep all night and I work all day.')

print('Yo')
print_lyrics()
x = x + 2
print(x)

#Greating in Different Languages
def greet(lang, nam):
    if lang == 'es':
        print('Hola' ,nam)
    elif lang == 'fr':
        print("Bonjour" , nam)
    else:
        print('Hello', nam)

name = input('What is your name?')
greet('en', name)
greet('fr', name)
greet('es', name)

#Arithmetic Function
def add(a, b):
    added = a + b
    return added

x = add(1, 2)
print(x)
