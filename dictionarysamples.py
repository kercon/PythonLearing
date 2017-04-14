myVehicle = {'wheels': 2, 'color': 'black', 'engine': 'disel'}


def dictBasic1():
    print(myVehicle)


def dictBasic2():
    print('print(myVehicle[\'color\'])', myVehicle['color'])


def dictBasic3():
    print('all values in list')
    for v in myVehicle.values():
        print(v, end=' ')
    print()
    print('all keys in list')
    for k in myVehicle.keys():
        print(k, end=' ')
    print()
    print('all items in list')
    for i in myVehicle.items():
        print(i, end=' ')
    print()


def dictBasic4():
    print('Get function')
    print('My vehicle have', str(myVehicle.get('wheels', 0)), 'wheels')
    print('My vehucle have', str(myVehicle.get('seatbelts', 0)), 'seatbelts')


def dictBasic5():
    message = 'The quick brown fox jumps over the lazy dog'
    count = {}
    print('Counting each aperrance of character in')
    print('\'The quick brown fox jumps over the lazy dog\'')
    print('by using count and setdefault')
    for character in message:
        count.setdefault(character, 0)
        count[character] += 1
    print(count)
