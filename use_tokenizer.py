from tokenizers import Tokenizer

tokenizer = Tokenizer.from_file("./tokenizer.json")

output = tokenizer.encode(open("./064/6400000.txt", "r").read())

print("\n")

print(output.tokens, end = "\n\n\n")

print(output.ids, end = "\n\n")

#waiting と runningは使わない
#judge id
#API request で　python から jsonファイル　language の条件を指定して(辞書型), status と　judge id をdataframeを抽出