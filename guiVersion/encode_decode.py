#module importing
from datasets import * 
from random import randint

def encode(string):
    new_string = ""

    # Generating settings for encode
    length = len(ALL_LETTERS_SHUFFLE) - 1
    length_d = len(DIGITS_SHUFFLE) - 1

    setting_list = [randint(0, length), randint(0, 7), randint(randint(0, 2), length_d)]
    setting = ".".join(str(n) for n in setting_list)

    set_1, set_2, set_3 = setting_list[0], setting_list[1], setting_list[2]

    # Encoding the string
    for letter in string:
        if letter in ALL_LETTERS:
            ind = ALL_LETTERS_SHUFFLE.index(letter)

            if set_1 + ind > length:
                add = (set_1 + ind) - length - 1
            else:
                add = set_1 + ind

            letter = ALL_LETTERS_SHUFFLE[add]
            new_string += letter

        elif letter == " ":
            letter = CHAR_LIST[set_2]
            new_string += letter

        elif letter in DIGITS_SHUFFLE:
            ind = DIGITS_SHUFFLE.index(letter)

            if set_3 + ind > length_d:
                add = (set_3 + ind) - length_d
            else:
                add = set_3 + ind

            letter = DIGITS_SHUFFLE[add]
            new_string += letter

        else:
            new_string += letter

        # Incrementing and checking settings
        set_1 += 1
        set_2 += 1

        if set_1 == length + 1:
            set_1 = 0
        if set_2 > 7:
            set_2 = 0

    return new_string, setting



def decode(string, setting):
    new_string = ""
    length = len(ALL_LETTERS_SHUFFLE) - 1
    length_d = len(DIGITS_SHUFFLE) - 1

    # Getting the settings to start decoding
    set_list = [int(n) for n in setting.split(".")]
    set_1, set_2, set_3 = set_list[0], set_list[1], set_list[2]

    # Decoding the string
    for letter in string:
        if letter in ALL_LETTERS:
            ind = ALL_LETTERS_SHUFFLE.index(letter)

            if ind - set_1 < 0:
                add = length - (set_1 - ind) + 1
            else:
                add = ind - set_1

            letter = ALL_LETTERS_SHUFFLE[add]
            new_string += letter

        elif letter in CHAR_LIST:
            letter = " "
            new_string += letter

        elif letter in DIGITS_SHUFFLE:
            ind = DIGITS_SHUFFLE.index(letter)

            if ind - set_3 < 0:
                add = length_d - (set_3 - ind) + 1
            else:
                add = ind - set_3

            letter = DIGITS_SHUFFLE[add]
            new_string += letter

        else:
            new_string += letter

        # Incrementing and checking settings
        set_1 += 1
        set_2 += 1

        if set_1 == length + 1:
            set_1 = 0
        if set_2 > 7:
            set_2 = 0

    return new_string


