import json
from tokenizers import Tokenizer

json_open = open('out.json', 'r')
json_load = json.load(json_open)

tokenizer = Tokenizer.from_file("./tokenizer.json")

data = []
for i in range(0, 100):
    input = tokenizer.encode(json_load[i][1])
    data.extend(input.ids)


def pre(l: list):
    for i in range(len(l) - 1):
        yield [l[:i + 1], l[i + 1]]

pairs = list(pre(data))

print(len(pairs))

