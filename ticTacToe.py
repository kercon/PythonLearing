import copy
import sys
import os
ClearBoard = {}


def setClearBoard():
    ClearBoard.setdefault('top-L', ' ')
    ClearBoard.setdefault('top-M', ' ')
    ClearBoard.setdefault('top-R', ' ')
    ClearBoard.setdefault('mid-L', ' ')
    ClearBoard.setdefault('mid-M', ' ')
    ClearBoard.setdefault('mid-R', ' ')
    ClearBoard.setdefault('low-L', ' ')
    ClearBoard.setdefault('low-M', ' ')
    ClearBoard.setdefault('low-R', ' ')


def printboard(board):
    print()
    print(board['top-L'], board['top-M'], board['top-R'], sep='|')
    print('-', '-', '-', sep='+')
    print(board['mid-L'], board['mid-M'], board['mid-R'], sep='|')
    print('-', '-', '-', sep='+')
    print(board['low-L'], board['low-M'], board['low-R'], sep='|', end='\n\n')


def checkwin(board, turn):
    win = False
    if (board['top-L'] == turn) and (board['top-M'] == turn):
        if(board['top-R'] == turn):
            win = True
    if (board['mid-L'] == turn) and (board['mid-M'] == turn):
        if (board['mid-R'] == turn):
            win = True
    if (board['low-L'] == turn) and (board['low-M'] == turn):
        if (board['low-R'] == turn):
            win = True
    if (board['top-L'] == turn) and (board['mid-L'] == turn):
        if (board['low-L'] == turn):
            win = True
    if (board['top-M'] == turn) and (board['mid-M'] == turn):
        if (board['low-M'] == turn):
            win = True
    if (board['top-R'] == turn) and (board['mid-R'] == turn):
        if (board['low-R'] == turn):
            win = True
    if (board['top-L'] == turn) and (board['mid-M'] == turn):
        if (board['low-R'] == turn):
            win = True
    if (board['top-R'] == turn) and (board['mid-M'] == turn):
        if (board['low-L'] == turn):
            win = True
    return win


def ticTacToe():
    os.system('cls')
    print('Welcome to Tic Tac Toe')
    print('Input Exit to Quit or Reset to start new game', end='\n')
    setClearBoard()
    while True:
        gameboard = copy.copy(ClearBoard)
        turn = 'X'
        correctcommand = False
        command = ' '
        for i in range(9):
            printboard(gameboard)
            print('Turn for', turn, 'Move on space?')
            correctcommand = False
            while not correctcommand:
                print('avaible moves:')
                for k in gameboard.keys():
                    if gameboard[k] == ' ':
                        print(k, end=' ')
                print()
                command = input()
                if ' ' == gameboard.get(command, '-'):
                    correctcommand = True
                if command == 'Exit':
                    sys.exit()
                if command == 'Reset':
                    break
            if command == 'Reset':
                break
            gameboard[command] = turn
            if checkwin(gameboard, turn):
                print('Winer:', turn)
                printboard(gameboard)
                break
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'
        print('Input Exit to stop')
        command = input()
        if command == 'Exit':
            break
        os.system('cls')
