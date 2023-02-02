import json
from tokenizers import Tokenizer
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

json_open = open('out.json', 'r')
json_load = json.load(json_open)

tokenizer = Tokenizer.from_file("./tokenizer2.json")


def pre(l: list):
    for i in range(len(l) - 1):
        yield [l[:i + 1], l[i + 1]]


pairs = []
for data in json_load:
    ids = tokenizer.encode(data[1]).ids
    pairs.extend(pre(ids))

import random
random.shuffle(pairs)

pairs = pairs[:10000]

from sklearn.model_selection import train_test_split 

traindata, testdata = train_test_split(pairs, train_size=0.9)

# nn.Moduleを継承して新しいクラスを作る。決まり文句
class LSTMClassifier(nn.Module):
    # モデルで使う各ネットワークをコンストラクタで定義
    def __init__(self, embedding_dim, hidden_dim, vocab_size, tagset_size):
        # 親クラスのコンストラクタ。決まり文句
        super(LSTMClassifier, self).__init__()
        # 隠れ層の次元数。これは好きな値に設定しても行列計算の過程で出力には出てこないので。
        self.hidden_dim = hidden_dim
        # インプットの単語をベクトル化するために使う
        self.word_embeddings = nn.Embedding(vocab_size, embedding_dim)
        # LSTMの隠れ層。これ１つでOK。超便利。
        self.lstm = nn.LSTM(embedding_dim, hidden_dim)
        # LSTMの出力を受け取って全結合してsoftmaxに食わせるための１層のネットワーク
        self.hidden2tag = nn.Linear(hidden_dim, tagset_size)
        # softmaxのLog版。dim=0で列、dim=1で行方向を確率変換。
        self.softmax = nn.LogSoftmax(dim=1)


    def forward(self, sentence):
        # 文章内の各単語をベクトル化して出力。2次元のテンソル
        embeds = self.word_embeddings(sentence)
        # 2次元テンソルをLSTMに食わせられる様にviewで３次元テンソルにした上でLSTMへ流す。
        # 上記で説明した様にmany to oneのタスクを解きたいので、第二戻り値だけ使う。
        _, lstm_out = self.lstm(embeds.view(len(sentence), 1, -1))
        # lstm_out[0]は３次元テンソルになってしまっているので2次元に調整して全結合。
        tag_space = self.hidden2tag(lstm_out[0].view(-1, self.hidden_dim))
        # softmaxに食わせて、確率として表現
        tag_scores = self.softmax(tag_space)
        return tag_scores




# traindata, testdata = train_test_split(pairs, train_size=0.8)

embedding_dim = 120
hidden_dim = 100
vocab_size = 600
tagset_size = 600

model = LSTMClassifier(embedding_dim, hidden_dim, vocab_size, tagset_size)

loss_function = nn.NLLLoss()

optimizer = optim.SGD(model.parameters(), lr=0.01)

from tqdm import tqdm
if __name__=="__main__":
        
    losses = []
    for epoch in tqdm(range(50)):
        all_loss = 0
        for data in tqdm(traindata, leave=False):
            # モデルが持ってる勾配の情報をリセット
            model.zero_grad()
            # 文章を単語IDの系列に変換（modelに食わせられる形に変換）
            mae = data[0]
            next = data[1]
            input_tensor = torch.tensor(mae, dtype=torch.long)
            # 順伝播の結果を受け取る
            out = model(input_tensor)
            # 正解カテゴリをテンソル化

            answer = torch.tensor([next], dtype=torch.long)
            answer = nn.functional.one_hot(answer, num_classes = vocab_size)
            # print(out.shape)
            # print(answer.shape)
            # 正解とのlossを計算

            loss = loss_function(out[0], answer[0])
            """
            loss = 0
            for j in range(out.size()[1]):
                loss += loss_function(out[j, :], answer[j, :])
            """


            # 勾配をセット
            loss.backward()
            # 逆伝播でパラメータ更新
            optimizer.step()
            # lossを集計
            all_loss += loss.item()
            # print(all_loss / (i + 1))

        losses.append(all_loss)
        file_name = f"./model_pth_{epoch}.pth"
        torch.save(model.state_dict(), file_name)

        print("epoch", epoch, "\t" , "loss", all_loss)
    print("done.")

    torch.save(model.state_dict(), './model.pth')
# 1 バッチ化　<- randomにした後に　pythorch
# 2 評価　不正解をモデルに入れてみる　-> 手動で見る