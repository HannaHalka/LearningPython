import random
import os
from time import sleep

medium_violet_red = '\033[95m'
bgcolor = '\033[38;5;1m'
orange_red = '\033[38;5;214m'
yellow = '\033[93m'
green = '\033[92m'
dark_turquoise = '\033[96m'
dark_blue = '\033[94m'
indigo = '\033[38;5;93m'
RESET = '\033[0m'


def clear_console():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def valid_input(coord):
    while True:
        input_coo = input(coord)
        if not input_coo.isdigit():
            print('Please enter numerical value!')
            continue
        int_coo = int(input_coo)
        if 4 < int_coo or int_coo < 1:  # we have 4x4 board
            print('Please enter number in interval 0-3!')
            continue
        return int_coo - 1



def init_board(size):
    symbols = ['@', '$', '%', '^', '&', '*', '#', '№'] * 2
    random.shuffle(symbols)
    secret_board = [symbols[i:i + size] for i in range(0, len(symbols), size)]
    return secret_board


def players_board(size):
    symbol = ['X'] * 16
    board = [symbol[i:i + size] for i in range(0, len(symbol), size)]
    return board


def display_field(board):
    for row in board:
        print('  '.join(row))


def open_card(board, secret_board, i, j):
    board[i][j] = secret_board[i][j]


def remove_cards(board, coords):
    for i, j in coords:
        board[i][j] = ' '


def card_is_not_removed(board):
    while True:
        row = valid_input('Please enter the row (1-4): ')
        col = valid_input('Please enter the column (1-4): ')
        if board[row][col] == ' ':
            print("This card is already removed!")
            continue
        return row, col


def win(board):
    for row in board:
        for item in row:
            if item != ' ':
                return False
    return True


secret_board = init_board(4)
# print(secret_board)  # debug

board = players_board(4)

your_rty = 0
while True:
    sleep(2)
    clear_console()
    print(display_field(board))

    i1, j1 = card_is_not_removed(board)
    i2, j2 = card_is_not_removed(board)

    if i1 == i2 and j1 == j2:
        print("You selected the same card twice! Try again")
        continue

    open_card(board, secret_board, i1, j1)
    open_card(board, secret_board, i2, j2)

    sleep(2)
    clear_console()
    print(display_field(board))

    if secret_board[i1][j1] == secret_board[i2][j2]:
        print('Congratulation its a match!')
        remove_cards(board, [(i1, j1), (i2, j2)])
    else:
        board[i1][j1], board[i2][j2] = 'X', 'X'

    your_rty += 1

    if win(board):
        clear_console()
        print(f"{medium_violet_red}{'C'}{bgcolor}{'on'}{orange_red}{'gr'}"
              f"{yellow}{'at'}{green}{'ul'}{dark_turquoise}{'at'}"
              f"{dark_blue}{'io'}{indigo}{'ns'}{medium_violet_red}{'!'}{RESET}",
              sep='', end=' ')
        print(f'You find all cards in {your_rty} try')
        break

