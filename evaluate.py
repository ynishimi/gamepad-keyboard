import json

result = open('result.txt')
answer = open('answer.txt')

count_correct = 0
count_wrong = 0
count_unk = 0
unk_dict: dict[str, int] = dict()
wrong_dict: dict[str, dict[str, int]] = dict()

for res_line, ans_line in zip(result, answer):
    for res_word, ans_word in zip(res_line.split(), ans_line.split()):
        if 'UNK' in res_word:
            count_unk += 1
            unk_dict[ans_word] = unk_dict.get(ans_word, 0) + 1
        elif res_word == ans_word:
            count_correct += 1
        else:
            count_wrong += 1
            wrong_dict_element =  wrong_dict.setdefault(ans_word, dict())
            wrong_dict_element[res_word] = wrong_dict_element.get(res_word, 0) + 1

accuracy = format(count_correct / (count_correct + count_wrong + count_unk) * 100, '.2f')
print(f'correct: {count_correct}, wrong: {count_wrong}, unknown: {count_unk}')
print(f'accuracy: {accuracy} %')

unk_dict_sorted = sorted(unk_dict.items(), key=lambda x: x[1], reverse=True)

with open('wrong_word_list.json', 'w') as f:
    json.dump(wrong_dict, f, indent=2)
with open('unk_word_list.json', 'w') as f:
    json.dump(unk_dict_sorted, f, indent=2)
