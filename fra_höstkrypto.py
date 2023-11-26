import sys

sys.setrecursionlimit(10000)

alt1 = {
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

alt2 = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'e',
    6: 'f',
    7: 'g',
    8: 'h',
    9: 'i',
    10: 'j',
    11: 'k',
    12: 'l',
    13: 'm',
    14: 'n',
    15: 'o',
    16: 'p',
    17: 'q',
    18: 'r',
    19: 's',
    20: 't',
    21: 'u',
    22: 'v',
    23: 'w',
    24: 'x',
    25: 'y',
    26: 'z',
    27: 'å',
    28: 'ä',
    29: 'ö'
}

alt3 = {
    2: 'a',
    3: 'b',
    4: 'c',
    5: 'd',
    6: 'e',
    7: 'f',
    8: 'g',
    9: 'h',
    10: 'i',
    11: 'j',
    12: 'k',
    13: 'l',
    14: 'm',
    15: 'n',
    16: 'o',
    17: 'p',
    18: 'q',
    19: 'r',
    20: 's',
    21: 't',
    22: 'u',
    23: 'v',
    24: 'w',
    25: 'x',
    26: 'y',
    27: 'z',
    28: 'å',
    29: 'ä',
    30: 'ö'
}

input1 = "114132712 19111514"
# bu 137 a17 a13 682 181 943 417
input2 = "120137017013682181943417"
output = ""


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
            output1 += alt1[int(string[:2])]
            char_check1(string[2:], output1)

        if 0 <= int(string[:1]):
            output += alt1[int(string[:1])]
            char_check1(string[1:], output)
        else:
            print("ABORTED                !!!")


def char_check2(string, output):
    if not string:
        print(output)
        return output

    if len(string) >= 2 and 1 <= int(string[:2]) < 29:
        output1 = output
        output1 += alt2[int(string[:2])]
        char_check2(string[2:], output1)

    if 1 <= int(string[:1]):
        output += alt2[int(string[:1])]
        char_check2(string[1:], output)
    else:
        print("ABORTED                !!!")


def char_check3(string, output):
    if not string:
        print(output)
        return output

    if len(string) >= 2 and 2 <= int(string[:2]) < 30:
        output1 = output
        output1 += alt3[int(string[:2])]
        char_check3(string[2:], output1)

    if 2 <= int(string[:1]):
        output += alt3[int(string[:1])]
        char_check3(string[1:], output)
    else:
        print("ABORTED                !!!")


words = input1.split()
print(words)
#print("\n" + "Alt1")
#for word in words:
#    print("----" + word + "----")
#    char_check1(word, output)

print("\n" + "Alt2")
for word in words:
    print("----" + word + "----")
    char_check2(word, output)

#print("\n" + "Alt3")
#for word in words:
#    print("----" + word + "----")
#    char_check3(word, output)


words2 = input2.split()
print("\n" + "Alt1")
for word in words2:
    print("----" + word + "----")
    char_check1(word, output)

#print("\n" + "Alt2")
#for word in words2:
#    print("----" + word + "----")
#    char_check2(word, output)

# 3an går ej på sista
