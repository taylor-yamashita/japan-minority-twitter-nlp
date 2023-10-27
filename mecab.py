import json
import MeCab
import demoji
import re

mt = MeCab.Tagger("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")

file = open('test-tweets.txt', 'r')

# we'll just test on a few tweets for now
for i in range(40):
    # load tweet, convert to py dict, access content
    tweet_json = file.readline()
    tweet_py = json.loads(tweet_json)
    tweet_text = tweet_py['rawContent'] # note: need other prop for over 140 char?

    # clean tweet content
    print("orig: ", tweet_text)
    remove_emojis = demoji.replace(tweet_text, "")
    remove_usernames = re.sub("@([a-zA-Z0-9_]+)", "", remove_emojis)
    remove_hashtags = re.sub("#([a-zA-Z0-9_ぁ-んァ-ン一-龠]+)", "", remove_usernames)
    remove_links = re.sub("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", "", remove_hashtags)
    
    # remove kaomoji; code from http://www.robfahey.co.uk/blog/tidying-japanese-sns-data-machine-learning/
    re_text = '[0-9A-Za-zぁ-ヶ一-龠]'
    re_nontext = '[^0-9A-Za-zぁ-ヶ一-龠]'
    re_allowtext = '[ovっつ゜ニノ三二]'
    re_hwkana = '[ｦ-ﾟ]'
    re_openbracket = r'[\(∩꒰（]'
    re_closebracket = r'[\)∩꒱）]'
    re_aroundface = '(?:' + re_nontext + '|' + re_allowtext + ')*'
    re_face = '(?!(?:' + re_text + '|' + re_hwkana + '){3,}).{3,}'
    kao_finder = re.compile(re_aroundface + re_openbracket + re_face + re_closebracket + re_aroundface)
    remove_kaomoji = kao_finder.sub("", remove_links)

    print("cleaned: ", remove_kaomoji, "\n")

    # mecab tokenization
    parsed = mt.parseToNode(remove_links)
    components = []
    while parsed:
        components.append(parsed.surface)
        parsed = parsed.next
    # print(components, "\n")