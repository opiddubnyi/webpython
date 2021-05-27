import pygame
import random


player = str(input("Enter player name: "))


def pick_word(difficulty, filename='10000_words.txt'):
    with open(filename, 'r') as file:
        words = file.readlines()
        interesting_word = False

        while not interesting_word:
            word = random.choice(words)
            if len(word) == difficulty:
                interesting_word = True
                return word


def obscure_word(word, guessed):
    reveal = ''
    for char in word:
        if char not in guessed:
            reveal += '_'
        else:
            reveal += char
    return reveal


def game_round():
    is_end = False
    guessed = []
    word = pick_word(int(input('Enter word length: ')))
    die_count = 7

    while not is_end and die_count:

        print('Guess this word:')
        print(obscure_word(word, guessed))
        print(f'So far tried {guessed}')
        print(f'You have {die_count} tries left')

        letter = str(input('Enter your guess, or "Exit" to quit: ')).lower()
        print('\n')

        if letter.isalpha() and len(letter) == 1:
            if letter in set(guessed):
                print("You've tried this one, enter a different letter.")
                continue
            if letter in word and letter not in guessed:
                print(f"Good job {player}, maybe you'll live today..")
            guessed.append(letter)

        elif letter == 'Exit':
            is_end = True
            print('Game over!')

        else:
            print('Try again:')

        if word == obscure_word(word, guessed):
            is_end = True
            print('Congratulations! You have another day to live..')

        if letter not in word:
            die_count -= 1

    print('Game over!')


print("You have 7 tries to guess the word, otherwise you'll die!\n"
      "Good luck!")

game_round()
