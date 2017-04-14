import copy


def refernce():
    spam = [0, 1, 2, 3, 4, 5]
    print("spam:", spam)
    cheese = spam
    print("cheese:", cheese)
    spam += [6]
    print("modified spam +=6")
    print("spam:", spam)
    print("cheese:", cheese)
    cheese.remove(2)
    print("modified cheese cheese.remove(2)")
    print("spam:", spam)
    print("cheese:", cheese)
    print()


def copysample():
    spam = [0, 1, 2, 3, 4, 5]
    print("spam:", spam)
    cheese = copy.copy(spam)
    print("cheese:", cheese)
    spam += [6]
    print("modified spam +=6")
    print("spam:", spam)
    print("cheese:", cheese)
    cheese.remove(2)
    print("modified cheese cheese.remove(2)")
    print("spam:", spam)
    print("cheese:", cheese)
    print()
