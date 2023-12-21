import sys
import copy

sys.setrecursionlimit(1000000)

nums = [
    [23, 6, 7, 12],
    [25, 8, 20, 21],
    [17, 2, 24, 29],
    [22, 9, 13, 18],
    [10, 11, 16, 14],
    [15, 21, 8, 3],
    [13, 31, 22, 32],
    [16, 11, 17, 24],
    [14, 10, 26, 27]
]

lets = [
    ['s', 't', 'u', 'v'],
    ['m', 'n', 'o', 'p'],
    ['a', 'b', 'c', 'd'],
    ['r', 'å', 'ä', 'ö'],
    ['e', 'f', 'g', 'h'],
    ['k', 'l', 'm', 'n'],
    ['x', 'y', 'r', 'å'],
    ['c', 'd', 'e', 'f'],
    ['g', 'h', 'i', 'j']
]

num_to_let = {}
final_dict = {}

secret = "10 – 7 – 6 – 23 – 2 – 12 – 13 – 11 – 6 – 11 – 13 – 26 – 8 – 20 – 13 – 10 – 20 – 21"

secret = secret.split(" – ")

# Strings which cancel recursion
check_strings = ["gtv", "gtu", "gvt", "gvu", "gst", "gsu", "gsv", "hvt", "gts", "gvs", "hvs", "hvu", "hts", "htu"
                 "hst", "hsv", "hsu", "hst", "htv", "hut", "huv", "guv", "htu", "gut"]


for row_num, row_let in zip(nums, lets):
    for num, let in zip(row_num, row_let):
        if num not in num_to_let:
            num_to_let[num] = set(row_let)
        else:
            # implement shared letters (intersect)
            num_to_let[num] = num_to_let[num].intersection(set(row_let))

def remove_let(dict, letter):
    dict_copy = copy.deepcopy(dict)
    for num, let in dict_copy.items():
        if letter in let:
            let.remove(letter)
    return dict_copy


def try_char(dict, final_dict, secret, org_secret):
    global check_strings

    current_output = ''.join([final_dict.get(int(num), '?') for num in org_secret])

    if any(current_output.startswith(s) for s in check_strings):
        return

    if not secret:
        print(current_output)

        if current_output == "gustavreserimorgon":
            print("Final dict :", final_dict)
            print("Dict:")
            for key, value in dict.items():
                print(f"{key}: {value}")

        return

    sec_num = secret[0]  # Current number to process

    for let in dict[int(sec_num)]:
        final_dict_copy = final_dict.copy()
        final_dict_copy[int(sec_num)] = let  # Update the final dict for the current letter
        dict_copy = remove_let(dict, let)  # Remove the letter from future consideration

        next_secret = [num for num in secret if num != sec_num]

        try_char(dict_copy, final_dict_copy, next_secret, org_secret)


print(secret)
for num, letters in num_to_let.items():
    print(f'{num}: {letters}')

try_char(num_to_let, final_dict, secret, secret)