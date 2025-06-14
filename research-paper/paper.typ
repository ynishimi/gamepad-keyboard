#import "lib/template.typ": *
#show: jarticle

= Introduction

= モデル

```sh
// コーパスを作成
python make_corpus.py

// モデルの学習
train-kytea -full train.txt -model train.mod

// 変換を行う。単語分割を行わないので -nows オプションを用いる。
kytea -model train.mod -nows < test.txt > result.txt

// 結果の分析
.venvnishimi@MacBook-Air-3 gamepad-keyboard % python evaluate.py
correct: 138914, wrong: 9068
accuracy: 93.87 %
```
