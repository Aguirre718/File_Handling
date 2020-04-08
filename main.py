# -*- coding: utf-8 -*-

def main():
    print('    Search a word in .txt file    ')

    word = str(input('Enter the word to be searched: '))
    find_word(word)

def find_word(word):
    counter = 0
    with open('texto.txt') as f:
        for line in f:
            counter += line.count(word)

    print('The word {} is in the text {} times'.format(word, counter))
    print('')

if __name__ == '__main__':
    main()