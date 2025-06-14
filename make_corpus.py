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
index = int(0.8 * len(sentences))
with open('train.txt', 'w') as f:
    for sentence in sentences[:index]:
        f.write(make_train_corpus(sentence) + '\n')
        
with open('test.txt', 'w') as f:
    for sentence in sentences[index:]:
            f.write(make_test_corpus(sentence) + '\n')
    
with open('answer.txt', 'w') as f:
    for sentence in sentences[index:]:
            f.write(make_answer_corpus(sentence) + '\n')