from tokenizers import Tokenizer, normalizers, pre_tokenizers
from tokenizers.models import WordLevel
from tokenizers.normalizers import NFD, Lowercase, StripAccents
from tokenizers.pre_tokenizers import Digits, Whitespace
from tokenizers.processors import TemplateProcessing
from tokenizers.trainers import WordLevelTrainer
import json

json_open = open('out.json', 'r')

json_load = json.load(json_open)

SMALL_TRAINING_CORPUS = []
SMALL_TRAINING_CORPUS.extend(i[1] for i in json_load)
print(len(SMALL_TRAINING_CORPUS))
#データ数2422
#データの重複を削除したい　（学習のコード数は200ぐらいでいい）
"""
for i in range(6400000, 6454000):
    i = str(i)
    f_name = "./064/" + i + ".txt"
    try:
        SMALL_TRAINING_CORPUS.append(open(f_name, "r").read())
    except FileNotFoundError:
        pass
    #[open("./064/6400000.txt", "r").read()]
"""

#　https://huggingface.co/robot-test/dummy-tokenizer-wordlevel
tokenizer = Tokenizer(WordLevel(unk_token="[UNK]"))
tokenizer.normalizer = normalizers.Sequence([NFD(), Lowercase(), StripAccents()])

tokenizer.pre_tokenizer = pre_tokenizers.Sequence([Whitespace(), Digits(individual_digits=True)])

tokenizer.post_processor = TemplateProcessing(
    single="[CLS] $A [SEP]",
    pair="[CLS] $A [SEP] $B:1 [SEP]:1",
    special_tokens=[
        ("[CLS]", 1),
        ("[SEP]", 2),
    ],
)

vocab_size = 400
trainer = WordLevelTrainer(vocab_size = 400, special_tokens=["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]"])

tokenizer.train_from_iterator(SMALL_TRAINING_CORPUS, trainer=trainer)

tokenizer.save("tokenizer.json")

# output = tokenizer.encode([open("./064/6400000.txt", "r").read()])
