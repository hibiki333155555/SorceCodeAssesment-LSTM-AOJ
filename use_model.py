import torch 
import torch.nn as nn
import train
import pandas as pd
from tokenizers import Tokenizer


embedding_dim = 10
hidden_dim = 100
vocab_size = 400
tagset_size = 400

model = train.LSTMClassifier(embedding_dim, hidden_dim, vocab_size, tagset_size)
model.load_state_dict(torch.load('./model.pth'))
model.eval()


tokenizer = Tokenizer.from_file("./tokenizer.json")
f_name = "test.txt"
test_tokens = tokenizer.encode([open(f_name, "r").read()])

def pre(l: list):
    for i in range(len(l) - 1):
        yield [l[:i + 1], l[i + 1]]

pairs = list(pre(test_tokens))


for test in pairs:
        mae = test[0]
        next = test[1]
        input_tensor = torch.tensor(mae, dtype=torch.long)
        # 順伝播の結果を受け取る
        out = model(input_tensor)
        answer = torch.tensor([next], dtype=torch.long)
        answer = nn.functional.one_hot(answer, num_classes = vocab_size)
        print(answer)
        print(out)