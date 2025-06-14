#import "lib/template.typ": *
#show: jarticle

= Introduction

= モデル

```sh
// モデルの学習
train-kytea -full train.txt -model train.mod
```

```sh
// 変換を行う。単語分割を行わないので -nows オプションを用いる。
kytea -model train.mod -nows < test.txt > result.txt
```
