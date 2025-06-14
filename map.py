from nltk.corpus import brown

BUTTON_MAPPING: dict[str, set[str]] = {
    # ' ': {' '},
    '0': {'q', 'a', 'z'},
    '1': {'w', 's', 'x'},
    '2': {'e', 'd', 'c'},
    '3': {'r', 'f', 'v'},
    '4': {'t', 'g', 'b'},
    '5': {'y', 'h', 'n'},
    '6': {'u', 'j', 'm'},
    '7': {'i', 'k'},
    '8': {'o', 'l'},
    '9': {'p'}
}

# def make_input(word: str) -> str:
#     input = ''
#     for char in word:
#         for key, vals in BUTTON_MAPPING.items():
#             if char in vals:
#                 input += key
#                 break
#     return input

# # '01234' = ['qwerty'] など
# input_dict: dict[str, set[str]] = dict()

# words: list[str] = reuters.words()[:20]
# for word in words:
#     word = word.lower()
#     if word.isalpha() and not word in input_dict.values():
#         input = make_input(word)
#         input_dict.setdefault(input, set()).add(word)

# # for input, dict_values in input_dict.items():
# #     if len(dict_values) > 1:
# #         print(input, dict_values)

# print(input_dict)


def make_train_corpus(sentence: str):
    corpus: list[str] = []
    for word in sentence:
        word = word.lower()
        input = ""
        if word.isalpha():
            for char in word:
                for key, vals in BUTTON_MAPPING.items():
                    if char in vals:
                        input += key
                        break
            corpus.append(input + '/' + word)
    return " ".join(corpus)

def make_test_corpus(sentence: str) -> str:
    corpus: list[str] = []
    for word in sentence:
        word = word.lower()
        input = ""
        if word.isalpha():
            for char in word:
                for key, vals in BUTTON_MAPPING.items():
                    if char in vals:
                        input += key
                        break
            corpus.append(input)
    return " ".join(corpus)

def make_answer_corpus(sentence: str) -> str:
    return make_train_corpus(sentence)

sentences = brown.sents()
print("---train---")
for sentence in sentences[:10]:
    print(make_train_corpus(sentence))

print("---test---")
for sentence in sentences[10:20]:
    print(make_test_corpus(sentence))

print("---answer---")
for sentence in sentences[10:20]:
    print(make_answer_corpus(sentence))