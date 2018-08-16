#ハングマンの関数モジュール
import random

def hangman(word):
    wrong = 0
    stages = ['',
              '______      ',
              '|     |     ',
              '|     |     ',
              '|     O     ',
              '|    /|\    ',
              '|    / \    ',
              '|           ']

    rletters = list(word)
    board = ['_'] * len(word)
    win = False
    print('Welcome to HANGMAN')

    while wrong < len(stages) - 1:
        print('\n')
        char = input('一文字を予想して:')
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$$$'
        else:
            wrong += 1
        print(' '.join(board))
        e = wrong + 1
        print('\n'.join(stages[0:e]))
        if '_' not in board:
            print('you are win')
            print(' '.join(board))
            win = True
            break
    if not win:
        print('you are lose. collect:{}'.format(word))

str_list = ['cat', 'fox', 'fire', 'book', 'car']
random = random.randint(0,4)
hangman(str_list[random])
