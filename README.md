# SorceCodeAssesment-LSTM-AOJ
##　目的
AOJから取得したsoruce_codeを学習しプログラミングコードのエラー検知モデルを作る。 
発表スライド:https://docs.google.com/presentation/d/1wgntSqGvJa_5tn8RrNulVyeR9755m6Rtl-PW5IaVnL4/edit?usp=sharing   
(2023/2/2)

## 概要
学習データには正解判定されたコード飲み使用する。
モデルは入力されたコードのトークンから次のコードを予測するもの。
予測に対して実際のコードの確率が低ければエラーとする。

1 souce code をトークン化  
2 教師あり学習を実現するためにコードのペアを作る。  
3 pytorchによるLSTMの実装  
4 学習


## out.json
AOJから入手したsource_codeの情報が入っている。  
(ALDS1-1A language:c++ status:AC)

## train_tokenizer 
source code をトークン化するための準備　-> tokenizer.json ファイルを出力  
再び実行する必要はない  

## tokenizer.json
train_tokenizer によって出力された jsonファイル 
  
tokenizer = Tokenizer.from_file("./tokenizer.json"). 
とすることで使用できる  
