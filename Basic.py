import random
import sys
import copy
import os
from liststuple import *
from references import *
from dictionarysamples import *
from ticTacToe import *
from regex import *
from files import *


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
    text = text.lower()
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
    if text == 'dict':
        dictBasic1()
        dictBasic2()
        dictBasic3()
        dictBasic4()
        dictBasic5()
    if text == 'tictactoe':
        ticTacToe()
    if text == 'regex':
        print(phonesearch('My number is 415-555-4242.').group())
        print('input text for search')
        searchtext = input()
        print('input mask for search')
        masktext = input()
        print('input mod all or first')
        modtext = input()
        print(regexrsearch(searchtext, masktext, modtext))
    if text == 'files':
        directory()
        makedirectory()
        getfiles()


while True:
    print('Type printsep to Print seperators samples')
    print('Type list to Print lists samples')
    print('Type tuple to Print tuple samples')
    print('Type ref to Print reference samples')
    print('Type copy to Print copy samples')
    print('Type dict to Print dictionary samples')
    print('Type tictactoe to play tictactoe sample')
    print('Type regex to Print Regular Expresion sample')
    print('Type exit to exit')
    response = input()
    os.system('cls')
    FunSelector(response)
