from tokenizers import Tokenizer, pre_tokenizers, decoders, processors
from tokenizers.models import BPE
from tokenizers.trainers import BpeTrainer
import json

json_open = open('out.json', 'r')

json_load = json.load(json_open)

SMALL_TRAINING_CORPUS = []
SMALL_TRAINING_CORPUS.extend(i[1] for i in json_load)
print(len(SMALL_TRAINING_CORPUS))
#データ数2422

#　https://huggingface.co/robot-test/dummy-tokenizer-wordlevel
tokenizer = Tokenizer(BPE(unk_token="[UNK]"))
# tokenizer.normalizer = normalizers.Sequence([NFD(), Lowercase(), StripAccents()])

tokenizer.pre_tokenizer = pre_tokenizers.ByteLevel(add_prefix_space=False)

tokenizer.decoder = decoders.ByteLevel()

tokenizer.post_processor = processors.ByteLevel(trim_offsets=False)

vocab_size = 600
trainer = BpeTrainer(vocab_size = 600, special_tokens=["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]"])

tokenizer.train_from_iterator(SMALL_TRAINING_CORPUS, trainer=trainer)

tokenizer.save("tokenizer2.json")
