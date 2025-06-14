import json

result = open('result.txt')
answer = open('answer.txt')

count_correct = 0
count_wrong = 0
wrong_dict: dict[str, list[str]] = dict()

for res_line, ans_line in zip(result, answer):
    for res_word, ans_word in zip(res_line.split(), ans_line.split()):
        if res_word == ans_word:
            count_correct += 1
        else:
            count_wrong += 1
            wrong_dict.setdefault(ans_word, list()).append(res_word)

accuracy = format(count_correct / (count_correct + count_wrong) * 100, '.2f')
print(f'correct: {count_correct}, wrong: {count_wrong}')
print(f'accuracy: {accuracy} %')

with open('wrong_word_list.json', 'w') as f:
    json.dump(wrong_dict, f, indent=2)
