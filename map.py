from nltk.corpus import reuters

BUTTON_MAPPING: dict[str, set[str]] = {
    ' ': {' '},
    '0': {'q', 'a', 'z'},
    '1': {'w', 's', 'x'},
    '2': {'e', 'd', 'c'},
    '3': {'r', 'f', 'v'},
    '4': {'t', 'g', 'b'},
    '5': {'y', 'h', 'n'},
    '6': {'u', 'j', 'm'},
    '7': {'i', 'k', ','},
    '8': {'o', 'l', '.'},
    '9': {'p', ';', '/'}
}

def make_input(word: str) -> str:
    input = ''
    for char in word:
        for key, vals in BUTTON_MAPPING.items():
            if char in vals:
                input += key
                break
    return input

# '01234' = ['qwerty'] など
input_dict: dict[str, set[str]] = dict()

words: list[str] = reuters.words()[:10000]
for word in words:
    word = word.lower()
    if word.isalpha() and not word in input_dict.values():
        input = make_input(word)
        input_dict.setdefault(input, set()).add(word)

for input, dict_values in input_dict.items():
    if len(dict_values) > 1:
        print(input, dict_values)