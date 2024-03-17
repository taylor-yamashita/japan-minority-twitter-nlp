import json
import MeCab
import demoji
import mojimoji
import re
from stopwords_ja import stop_words
from stopwords_slothlib import stop_words_2
import gensim, logging

# cleaning and tokenizing
mt = MeCab.Tagger("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
file = open('test-tweets.txt', 'r')

# we'll just test on a few tweets for now
tweets = []
for i in range(100):
    # load tweet, convert to py dict, access content
    tweet_json = file.readline()
    tweet_py = json.loads(tweet_json)
    text = tweet_py['rawContent'] # note: need other prop for over 140 char?

    # clean tweet content
    # from https://colab.research.google.com/drive/1bX-JyY4xmCm_RFkJg3QNcthUvEJaBghP
    # handle half-width/full-width chars, jp punctuation
    text = text.lower()
    text = mojimoji.zen_to_han(text, kana=False)
    text = mojimoji.han_to_zen(text, digit=False, ascii=False)
    text = text.translate(str.maketrans({
        '!': '！', '"': '”', '#': '＃', '$': '＄', '%': '％', '&': '＆', '\'': '’',
        '(': '（', ')': '）', '*': '＊', '+': '＋', ',': '，', '-': '−', '.': '．',
        '/': '／', ':': '：', ';': '；', '<': '＜', '=': '＝', '>': '＞', '?': '？',
        '@': '＠', '[': '［', '\\': '＼', ']': '］', '^': '＾', '_': '＿', '`': '｀',
        '{': '｛', '|': '｜', '}': '｝'
        }))
    zenkaku_leftsingle = b'\xe2\x80\x98'.decode('utf-8')
    text = re.sub('[’´｀]', zenkaku_leftsingle, text)
    
    # remove twitter-specific strings (handles, hashtags, etc.)
    text = re.sub("@([a-zA-Z0-9_]+)", "", text)
    text = re.sub("#([a-zA-Z0-9_ぁ-んァ-ン一-龠]+)", "", text)
    text = re.sub("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", "", text)

    # remove emojis
    text = demoji.replace(text, "")
    text = re.sub("([\uD83E-\uD83E])+", "", text)

    # remove punctuation and whitespace
    text = re.sub("([^一-龯ぁ-んァ-ン])+","",text)  
    text = re.sub("(\s)+", "", text)

    # mecab tokenization
    parsed = mt.parseToNode(text)
    components = []
    while parsed:
        word = parsed.surface
        pos = parsed.feature.split(",")[0]

        # remove beg/end tokens, particles, fillers, auxiliary bound prefixes/endings
        exclude_pos = ['BOS/EOS', '助詞', 'フィラー', '接頭詞', '助動詞']
        if pos not in exclude_pos: components.append(word)
        parsed = parsed.next

    # remove additional stopwords
    components = [token for token in components if ((not token in stop_words) and (not token in stop_words_2))]
    tweets.append(components)
    
# word2vec

# set up logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# train word2vec
model = gensim.models.Word2Vec(tweets, min_count=3)

# check similarity given by trained model
sim = model.wv.most_similar('今日')
# print(sim)

top_50 = model.wv.index_to_key[:50]
# for word in top_50:
#     print(word)