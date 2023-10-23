import json
import MeCab

mt = MeCab.Tagger("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")

# use our jan 2022 txt file 
file = open('2022-all/2022-01.txt', 'r')

# we'll just test on a few tweets for now
for i in range(5):
    # load tweet, convert to py dict, access content
    tweet_json = file.readline()
    tweet_py = json.loads(tweet_json)
    tweet_text = tweet_py['rawContent']

    # will need to clean content - links, usernames, hashtags, etc.

    # mecab tokenization
    parsed = mt.parseToNode(tweet_text)
    components = []
    while parsed:
        components.append(parsed.surface)
        parsed = parsed.next
    print(components)