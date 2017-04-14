import random
import sys


def ExitFunction():
    print('Bye Bye')
    sys.exit()


def Printseperators():
    print('print(\'cats\',\'dogs\',\'mice\')')
    print('cats', 'dogs', 'mice')
    print()
    print('print(\'cats\',\'dogs\',\'mice\',sep=\',\')')
    print('cats', 'dogs', 'mice', sep=',')
    print()


def Lists():
    number = 1
    names = []
    print('input names, empty name will end loop')
    while True:
        print('Name', number, ':', end='')
        name = input()
        if name == '':
            break
        names += [name]
        number += 1
    print('Inputed Names')
    for name in names:
        print(name, end=' ')
    print()
    print('Input name to check if name is in list')
    name = input()
    if name in names:
        print('names is in list on position:', names.index(name))
    else:
        print('name not in list')


def FunSelector(text):
    if text == 'exit':
        ExitFunction()
    if text == 'printsep':
        Printseperators()
    if text == 'list':
        Lists()


while True:
    print('Type printsep to Print seperators samples')
    print('Type list to Print lists samples')
    print('Type exit to exit')
    response = input()
    FunSelector(response)
