import random
import sys
import copy
from Liststuple import *
from references import *


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


def FunSelector(text):
    if text == 'exit':
        ExitFunction()
    if text == 'printsep':
        Printseperators()
    if text == 'list':
        Lists()
    if text == 'tuple':
        Tuplesample()
    if text == 'ref':
        refernce()
    if text == 'copy':
        copysample()


while True:
    print('Type printsep to Print seperators samples')
    print('Type list to Print lists samples')
    print('Type tuple to Print tuple samples')
    print('Type ref to Print reference samples')
    print('Type copy to Print copy samples')
    print('Type exit to exit')
    response = input()
    FunSelector(response)
