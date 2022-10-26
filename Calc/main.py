# @TODO comment

a = 0
b = 0

def sum(a, b):
    return a + b

a = int(input('Enter a = '))
b = int(input('Enter b = '))
o = input('Choose operation (+ | - | * | / | // | ** | % ): ')

if o == '+':
    print('a + b = ', sum(a, b))
elif o == '-':
    print('a - b = ', a - b)
else:
    print('Invalide enter')

