from random import randint

keys = [
    ['I', 'N', '&', 'U', 'y', 'v', 'x', '0', 'k', 'C', 'A', 'c', 'd', ')', 'f', 'a', '2', 'O', '1', 'S', 'n', 'X', '(',
     '4', '5', 'Y', 'H', '+', 'm', 'w', 'j', 't', '6', '8', 'R', 'b', 'F', 'Q', '7', '$', 'z', 'l', 's', 'J', 'M', 'e',
     'o', '!', 'P', 'r', 'T', 'i', 'h', 'G', 'D', '#', 'g', 'W', 'Z', 'B', 'u', '%', 'V', '9', 'E', 'K', '*', '3', 'L',
     'p', 'q'],
    ['v', '8', '!', 'j', 'T', 'A', '&', '+', 'S', 'O', 'W', 'l', 'M', 'e', '1', 'C', '%', 'u', '*', '(', 'y', 'c', 's',
     'r', 'V', 'm', 'U', 'b', 'D', 'E', 'N', 'f', 'q', ')', 'X', 'G', 'Y', 'k', 'p', 'I', 'h', 'g', 'w', '3', 'Z', 'a',
     '6', '$', 'o', '2', 'H', '4', '9', 'd', '7', 'z', '0', 'R', 'n', 'J', '5', 'Q', 'B', 't', '#', 'L', 'K', 'F', 'x',
     'P', 'i'],
    ['V', 'Q', 'I', 'y', 's', 'o', '&', 'D', 'w', 'x', 'i', 'm', '0', 'E', 'X', 'O', '4', '%', 'd', 'A', 'c', 'R', 'e',
     't', 'q', 'U', 'g', '1', 'W', 'v', 'G', '#', 'h', 'S', '3', 'H', 'r', '8', 'P', '$', ')', '!', 'L', 'K', 'u', 'n',
     '9', '+', 'a', 'Y', '6', '(', 'k', 'B', 'N', 'l', '7', '5', 'Z', 'C', 'T', 'b', 'p', '*', 'f', 'F', 'z', 'j', 'J',
     'M', '2'],
    ['6', 'g', 'U', '5', ')', 'A', 'O', '$', 'c', '!', 'W', 'Z', '9', '1', 'q', '3', 'M', 'p', 'T', 'f', 't', '4', 'P',
     'I', '8', 'X', 'E', 'D', 'n', 'b', 'S', 'x', 'h', 'w', 'R', 'u', 'o', 'K', 'y', 'j', 'i', 'Y', 'r', 'd', 'V', '7',
     'e', '#', '+', 'F', '2', 'J', 'B', '%', 'v', 'G', 'z', '&', 'H', 'a', 's', '(', '*', 'l', 'k', '0', 'C', 'Q', 'm',
     'N', 'L'],
    ['G', '3', 'T', 'K', 'U', '6', 'n', 's', 'L', 'b', '5', 'x', 'B', 'v', 'h', 'w', 'O', 'D', 'u', 'H', '9', 'S', '1',
     'C', 'E', 'R', 'y', 'z', 'o', '4', '&', '$', '7', '0', 'i', 'A', 'W', 'l', 'J', 'p', '#', '8', 'X', ')', 't', 'N',
     '%', 'Q', 'c', '+', 'Z', '(', 'q', '2', '!', 'P', 'e', 'a', 'F', 'M', 'd', 'I', 'm', 'r', 'Y', 'j', 'V', 'k', 'f',
     'g', '*'],
    ['3', 'w', 'd', 'q', '$', 'x', 'm', '0', 'C', 'E', 'R', 'G', '1', '9', 'g', 'H', 'u', 'F', 'l', 'r', '6', 'Z', 'M',
     '%', ')', 'J', 'k', 't', 'S', 'e', 'X', 'K', 'z', '&', 'W', '5', 'T', '8', '(', 'O', 'A', 'Q', 'y', 'N', 'a', 'I',
     'B', '7', 'P', 'V', 'p', 'f', '!', 'c', '*', 'j', 'i', '4', '+', 'L', 'n', 'o', 'v', 'h', '#', 'U', '2', 'b', 's',
     'D', 'Y'],
    ['d', 'F', '7', 't', 'P', 'A', 'S', '8', '1', 's', 'H', 'M', '3', 'u', 'X', '9', 'g', 'q', 'y', 'C', 'G', 'I', 'n',
     '%', 'T', 'c', 'Z', 'p', 'j', '+', 'f', '4', 'a', 'z', 'o', 'm', 'V', 'k', 'x', 'v', 'J', 'W', 'Y', 'U', '2', '(',
     '!', '$', 'r', 'D', 'b', 'h', 'E', '*', 'w', 'L', '#', 'i', 'l', 'Q', 'e', 'O', 'N', 'B', ')', 'K', '&', '0', '6',
     '5', 'R'],
    ['q', 'S', '!', 'D', 'j', 'y', 'b', '3', 's', 'Q', '7', 'u', 'w', '0', 'v', 'C', 'z', '*', 'M', 'K', 'W', ')', 'N',
     't', '#', 'h', 'E', 'H', '&', 'R', '1', '4', '$', 'J', '8', '6', 'l', 'm', 'T', 'V', 'a', '2', 'P', 'p', 'G', 'A',
     'o', '+', 'd', 'i', 'B', 'F', '9', '%', 'O', '5', '(', 'r', 'X', 'k', 'I', 'x', 'n', 'U', 'Z', 'c', 'L', 'f', 'Y',
     'g', 'e'],
    ['l', 'X', 'I', 'E', '+', 'J', '3', 'G', '(', 't', 'd', 'F', ')', 'c', '#', 'Q', '5', 'w', 'h', '8', 'e', 'g', 'A',
     'j', 'S', '*', 'u', 's', '9', 'M', 'q', 'N', 'r', 'v', 'T', 'C', 'f', 'W', 'Z', 'y', 'L', '&', 'p', '2', 'H', 'O',
     'm', 'x', 'B', 'k', '4', '6', 'o', 'D', '!', 'n', 'V', 'a', 'i', 'U', 'R', '1', 'z', 'K', 'b', 'Y', '$', '7', '%',
     'P', '0'],
    ['s', '7', 'j', 'z', 'D', 'n', 'J', '(', 'Z', '$', '#', '2', 'C', 'r', 'a', 'T', 'y', 'q', 'P', '+', 'f', '6', 'o',
     '0', 'i', 'b', 'g', 'I', 'w', 'S', '!', 'e', 'v', 'K', 'x', 'G', 'W', 'Q', 'M', ')', 'u', '8', 'p', 'O', 'B', '4',
     'h', '*', 'E', '%', '3', 'k', 'c', 'V', 't', 'N', 'm', 'l', '5', 'U', 'F', 'A', '1', '&', 'd', 'R', 'L', '9', 'H',
     'X', 'Y']]


def encode(txt):
    key_index = randint(0, 9)
    key = keys[key_index].copy()
    shift_amount = randint(1, len(key) - 1)
    txt = list(txt)
    result = str()
    for i in range(len(txt)):
        char = txt[i]
        char_index = key.index(char)
        new_char_index = (char_index + shift_amount) % len(key)
        new_char = key[new_char_index]
        result += new_char
    result += str(key_index)
    result += str(shift_amount).rjust(2, '0')
    return result


def decode(txt):
    key_index = int(txt[-3])
    key = keys[key_index]
    shift_amount = int(txt[-2:])
    txt = txt[:-3]
    result = str()
    for i in range(len(txt)):
        char = txt[i]
        char_index = key.index(char)
        new_char_index = char_index - shift_amount
        new_char = key[new_char_index]
        result += new_char
    return result
