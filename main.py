import collections

# The text provided to decipher
CIPHERTEXT = """
lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi
bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr jx
ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr
yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk
lmird jk xjubt trmui jx ibndt

wb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi
iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj ower m
vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mkd
wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr

jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii
ijnkd mkd ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh
mnbpjuwbt Inb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb
bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd
wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr
riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb
"""

# key mapping based on logical substitution
key = {
    'l': 'b', 'r': 'e', 'v': 'c', 'm': 'a', 'n': 'u',
    'i': 's', 'b': 't', 'p': 'h', 's': 'p', 'u': 'r',
    'w': 'i', 'j': 'o', 'x': 'f', 'q': 'k', 'y': 'm',
    'e': 'v', 'k': 'n', 'h': 'l', 'd': 'd', 't': 'y',
    'a': 'x', 'c': 'w', 'f': 'q', 'g': 'z', 'o': 'g'
}

def decrypter(text, mapping):
    """
    1. Iterates through every character in the ciphertext.
    2. Checks char exists in the key also converted to lowercase for the lookup.
    3. If TRUE -> substitutes FALSE --> keeps the original.
    """
    result = []
    for char in text:
        #Convert char to lowercase only for the lookup.
        # used once since the cipher text contains only 1 uppercase
        lower_char = char.lower()

        if char.isalpha() and lower_char in mapping:
            # When  match, append the substitution
            result.append(mapping[lower_char])
        else:
            # No match ,punctuation, space, or unmapped letter goes here keeping original
            result.append(char)

    return "".join(result)

# calls the decrypter passing in the ciphertext and the key
print(decrypter(CIPHERTEXT, key))