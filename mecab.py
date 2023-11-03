import json
import MeCab
import demoji
import re
from stop_words import stop_words
import gensim, logging

# cleaning and tokenizing

mt = MeCab.Tagger("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
file = open('test-tweets.txt', 'r')

# we'll just test on a few tweets for now
tweets = []
for i in range(40):
    # load tweet, convert to py dict, access content
    tweet_json = file.readline()
    tweet_py = json.loads(tweet_json)
    tweet_text = tweet_py['rawContent'] # note: need other prop for over 140 char?

    # clean tweet content
    remove_emojis = demoji.replace(tweet_text, "")
    remove_usernames = re.sub("@([a-zA-Z0-9_]+)", "", remove_emojis)
    remove_hashtags = re.sub("#([a-zA-Z0-9_ぁ-んァ-ン一-龠]+)", "", remove_usernames)
    remove_links = re.sub("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", "", remove_hashtags)
    remove_punc = re.sub("([.,、、。…「」!！?？~〜@#$%^&*():\{\}\[\]\/\\\\]+)", "", remove_links)

    # mecab tokenization
    parsed = mt.parseToNode(remove_punc)
    components = []
    while parsed:
        components.append(parsed.surface)
        parsed = parsed.next
    components = [token for token in components if not token in stop_words]
    tweets.append(components)

print(tweets)

# word2vec

# set up logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

model = gensim.models.Word2Vec(tweets, min_count=5)