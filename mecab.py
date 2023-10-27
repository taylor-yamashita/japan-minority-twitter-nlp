import json
import MeCab
import demoji
import re

mt = MeCab.Tagger("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")

file = open('test-tweets.txt', 'r')

# we'll just test on a few tweets for now
for i in range(50):
    # load tweet, convert to py dict, access content
    tweet_json = file.readline()
    tweet_py = json.loads(tweet_json)
    tweet_text = tweet_py['rawContent'] # note: need other prop for over 140 char?

    # clean tweet content
    print("orig: ", tweet_text)
    remove_emojis = demoji.replace(tweet_text, "")
    # print("no emoji: ", remove_emojis)

    remove_usernames = re.sub("@([a-zA-Z0-9_]+)", "", remove_emojis)
    # print("no usernames: ", remove_usernames)

    remove_hashtags = re.sub("#([a-zA-Z0-9_ぁ-んァ-ン一-龠]+)", "", remove_usernames)
    # print("no hashtags: ", remove_hashtags)
    
    remove_links = re.sub("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", "", remove_hashtags)
    # print("no links: ", remove_links)
    print("cleaned: ", remove_links, "\n")

    # mecab tokenization
    parsed = mt.parseToNode(remove_links)
    components = []
    while parsed:
        components.append(parsed.surface)
        parsed = parsed.next
    # print(components, "\n")