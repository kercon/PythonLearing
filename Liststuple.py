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


def Tuplesample():
    number = 1
    names = ()
    print('input names, empty name will end loop')
    while True:
        print('Name', number, ':', end='')
        name = input()
        if name == '':
            break
        names += name,
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
