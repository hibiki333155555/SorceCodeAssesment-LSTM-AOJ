import torch 
import torch.nn as nn
import train
import pandas as pd
import numpy as np
from tokenizers import Tokenizer

<<<<<<< HEAD

embedding_dim = 120
hidden_dim = 100
vocab_size = 600
tagset_size = 600

model = train.LSTMClassifier(embedding_dim, hidden_dim, vocab_size, tagset_size)
model.load_state_dict(torch.load("./model_pth_0.pth"))
model.eval()


tokenizer = Tokenizer.from_file("./tokenizer.json")
f_name = "./test.txt"
test_tokens = tokenizer.encode(open(f_name, "r").read())

=======
>>>>>>> c0e9b85a1cc9433f2faed570ef67e3a75765043e
def pre(l: list):
    for i in range(len(l) - 1):
        yield [l[:i + 1], l[i + 1]]

def probability_error_source_code(source_code):
    embedding_dim = 10
    hidden_dim = 100
    vocab_size = 600
    tagset_size = 600

<<<<<<< HEAD
for test in pairs:
        mae = test[0]
        next = test[1]
        input_tensor = torch.tensor(mae, dtype=torch.long)
        # 順伝播の結果を受け取る
        out = model(input_tensor)
        out2 = torch.argmax(out[0])
        out = out[0][next]
    
        out = torch.exp(out)
        # answer = torch.tensor([next], dtype=torch.long)
        # answer = nn.functional.one_hot(answer, num_classes = vocab_size)
        print(next)
        print(out.item())
        # print(out2)
=======
    model = train.LSTMClassifier(embedding_dim, hidden_dim, vocab_size, tagset_size)
    model.load_state_dict(torch.load("./model.pth"))
    model.eval()


    tokenizer = Tokenizer.from_file("./tokenizer.json")
    # f_name = "./test.txt"
    # test_tokens = tokenizer.encode(open(f_name, "r").read())
    test_tokens = tokenizer.encode(source_code)

    pairs = list(pre(test_tokens.ids))

    for test in pairs:
            mae = test[0]
            next = test[1]
            input_tensor = torch.tensor(mae, dtype=torch.long)
            # 順伝播の結果を受け取る
            out = model(input_tensor)
            out2 = torch.argmax(out[0])
            out = out[0][next]
            out = torch.exp(out)
            # answer = torch.tensor([next], dtype=torch.long)
            # answer = nn.functional.one_hot(answer, num_classes = vocab_size)
            print(next)
            print(out.item())
            print(out2)
>>>>>>> c0e9b85a1cc9433f2faed570ef67e3a75765043e
