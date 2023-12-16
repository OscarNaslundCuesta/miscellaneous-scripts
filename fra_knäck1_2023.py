import sys

sys.setrecursionlimit(10000)

digit_to_letter = {
    0: 'a',
    1: 'b',
    2: 'c',
    3: 'd',
    4: 'e',
    5: 'f',
    6: 'g',
    7: 'h',
    8: 'i',
    9: 'j',
    10: 'k',
    11: 'l',
    12: 'm',
    13: 'n',
    14: 'o',
    15: 'p',
    16: 'q',
    17: 'r',
    18: 's',
    19: 't',
    20: 'u',
    21: 'v',
    22: 'w',
    23: 'x',
    24: 'y',
    25: 'z',
    26: 'å',
    27: 'ä',
    28: 'ö'
}


def char_check1(string, output):
    if not string:
        print(output)
        return output

    if string[:1].isalpha():
        output += string[:1]
        char_check1(string[1:], output)
    else:
        if len(string) >= 2 and 0 <= int(string[:2]) < 28:
            output1 = output
            output1 += digit_to_letter[int(string[:2])]
            char_check1(string[2:], output1)

        if 0 <= int(string[:1]):
            output += digit_to_letter[int(string[:1])]
            char_check1(string[1:], output)
        else:
            print("ABORTED                !!!")


def translate_letters_to_digits(input_string, translation_dict):
    output = ""
    for char in input_string:
        if char.isalpha():
            if char in translation_dict:
                output += str(translation_dict[char])
            else:
                output += char
        else:
            output += char
    return output


letter_to_digit = {
    'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5,
    'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11,
    'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17,
    's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23,
    'y': 24, 'z': 25, 'å': 26, 'ä': 27, 'ö': 28
}

input_str = "cabjbhcabibjbdibdgebd bebjibbbbbhcgcbabbig fchbh cbibdbjebhbehbecb"
output = ""
translated_str = translate_letters_to_digits(input_str, letter_to_digit)

words = translated_str.split()
print(words)

for word in words:
    print("\n----" + word + "----")
    char_check1(word, output)

# utrustningen otillråcklig fär vinterbehov

