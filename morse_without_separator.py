morse_dict = { 'A':'.-', 'B':'-...',
'C':'-.-.', 'D':'-..', 'E':'.',
'F':'..-.', 'G':'--.', 'H':'....',
'I':'..', 'J':'.---', 'K':'-.-',
'L':'.-..', 'M':'--', 'N':'-.',
'O':'---', 'P':'.--.', 'Q':'--.-',
'R':'.-.', 'S':'...', 'T':'-',
'U':'..-', 'V':'...-', 'W':'.--',
'X':'-..-', 'Y':'-.--', 'Z':'--..',
'Å':'.--.-', 'Ä':'.-.-', 'Ö':'---.',
',':'--..--', '.':'.-.-.-', '?':'..--..' }

morse_dict2 = { '.-':'A', '-...':'B',
'-.-.':'C', '-..':'D', '.':'E',
'..-.':'F', '--.':'G', '....':'H',
'..':'I', '.---':'J', '-.-':'K',
'.-..':'L', '--':'M', '-.':'N',
'---':'O', '.--.':'P', '--.-':'Q',
'.-.':'R', '...':'S', '-':'T',
'..-':'U', '...-':'V', '.--':'W',
'-..-':'X', '-.--':'Y', '--..':'Z',
'.--.-':'Å', '.-.-':'Ä', '---.':'Ö',
'--..--':',', '.-.-.-':'.', '..--..':'?'}

morse_list = [
    '...----.-.-.-..-.-....---..-.-..-.',
    '......---....-.--..-.-.----...-...-...-',
    '..-...-......-------.-.-....-......-',
    '-----.-.....-.....-...-...----.-...-...',
    '-....-....-.-.-.-.-.....-...-...-...-.---.-.-.-.-..-',
    '......-..-.--...-.-.-.-.-',
    '--...--...-....-....-...--.--...--.',
]

cleartext = ''
morse_string = '' #enter string (for encryptor function)
decrypted = ''

with open("barnvisor.txt", "r", encoding="utf-8") as input:
    lines = input.readlines()

def encryptor():
    for line in lines:
        line = line.strip().upper()
        #print(line)
        enc_string = ""
        for char in line:
            if char in morse_dict:
                enc_string += morse_dict[char]
        if enc_string in morse_list:
            print(enc_string, line)


def decryptor(morse, decrypted): 

    if morse[:1] in morse_dict.values():
        morse_char = morse[:1]
        dec_char = morse_dict2[morse_char]
        decrypted += dec_char

        morse = morse[1:]

        decryptor(morse, decrypted)
    
    if morse[:2] in morse_dict.values():
        morse_char = morse[:2]
        dec_char = morse_dict2[morse_char]
        decrypted += dec_char

        morse = morse[2:]

        decryptor(morse, decrypted)

    if morse[:3] in morse_dict.values():

        morse_char = morse[:3]
        dec_char = morse_dict2[morse_char]
        decrypted += dec_char

        morse = morse[3:]

        decryptor(morse, decrypted)

    if morse[:4] in morse_dict.values():
        morse_char = morse[:4]
        dec_char = morse_dict2[morse_char]
        decrypted += dec_char

        morse = morse[4:]

        decryptor(morse, decrypted)

    if len(morse) == 0:
        f = open("output.txt", "a")
        f.write(decrypted + "\n")
        f.close()

#decryptor(morse_string, decrypted)
encryptor()