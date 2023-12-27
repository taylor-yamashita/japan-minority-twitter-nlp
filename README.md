# thesis

### requirements
install MeCab, demoji, gensim, mojimoji via pipenv.

### to load + use my pretrained word2vec models
For model trained on 2015 tweet dataset: `model = gensim.models.Word2Vec.load("thesis_w2v_2015_tweets")`

For model trained on 2022 tweet dataset: `model = gensim.models.Word2Vec.load("thesis_w2v_2022_tweets")`
