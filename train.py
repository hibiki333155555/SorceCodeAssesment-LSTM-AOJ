import json
from tokenizers import Tokenizer
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

json_open = open('out.json', 'r')
json_load = json.load(json_open)

tokenizer = Tokenizer.from_file("./tokenizer2.json")

# 学習用データはout.jsonの2242コード中100コード
data = []
for i in range(0, 100):
    input = tokenizer.encode(json_load[i][1])
    data.extend(input.ids)


def pre(l: list):
    for i in range(len(l) - 1):
        yield [l[:i + 1], l[i + 1]]

# pairsは合計18873組
pairs = list(pre(data))


from torch.utils.data import Dataset

class ErrorCorrectionDataset(Dataset):
    def __init__(self, pairs, train=True):
        # train:test = 9:1
        ratio = 0.9
        size = len(pairs)
        boundary = int(size * ratio)

        # 前半を train データ、後半を test データに分割
        if train:
            self.pairs = pairs[:boundary]
        else:
            self.pairs = pairs[boundary:]

    def __len__(self):
        return len(self.pairs)

    def __getitem__(self, idx):
        wa, ac = self.pairs[idx]
        return (torch.tensor(wa), torch.tensor(ac))

from torch.utils.data import DataLoader

batch_num = 128

train_data = ErrorCorrectionDataset(pairs, train=True)
test_data = ErrorCorrectionDataset(pairs, train=False)

train_dataloader = DataLoader(train_data, batch_size = batch_num, shuffle = True)
test_dataloader = DataLoader(test_data, batch_size = batch_num, shuffle = False)

train_size = len(train_data)
test_size = len(test_data)


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


from sklearn.model_selection import train_test_split


# traindata, testdata = train_test_split(pairs, train_size=0.8)

embedding_dim = 10
hidden_dim = 100
vocab_size = 600
tagset_size = 600

model = LSTMClassifier(embedding_dim, hidden_dim, vocab_size, tagset_size)

loss_function = nn.NLLLoss()

optimizer = optim.SGD(model.parameters(), lr=0.01)

if __name__=="__main__":
        
    losses = []
    for epoch in range(50):
        all_loss = 0
        for i in range(100):
            # モデルが持ってる勾配の情報をリセット
            model.zero_grad()
            # 文章を単語IDの系列に変換（modelに食わせられる形に変換）
            mae = train_data[i][0]
            next = train_data[i][1]
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
            # 勾配をセット
            loss.backward()
            # 逆伝播でパラメータ更新
            optimizer.step()
            # lossを集計
            all_loss += loss.item()
            # print(all_loss / (i + 1))
        losses.append(all_loss)
        print("epoch", epoch, "\t" , "loss", all_loss)
    print("done.")

    torch.save(model.state_dict(), './model.pth')
# 1 バッチ化　<- randomにした後に　pythorch
# 2 評価　不正解をモデルに入れてみる　-> 手動で見る