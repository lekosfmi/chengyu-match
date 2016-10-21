# Matching methods

from random import shuffle
from vocab.chin import chin_chengyu
from vocab.eng import eng_chengyu

# Shuffle the vocabularies
shuffle(chin_chengyu)
shuffle(eng_chengyu)


def eng_match():
    for i in range(len(chin_chengyu)):

        print("### " + chin_chengyu[i] + " ###")
        user_input = input("> ")

        if user_input == eng_chengyu[i]:
            print('⭕️')


def chin_match():
    for i in range(len(eng_chengyu)):

        print("### " + eng_chengyu[i] + " ###")
        user_input = input("> ")

        if user_input == chin_chengyu[i]:
            print('⭕️')
