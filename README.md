# Code for Questioning “Japanese-ness”: A Holistic Analysis of Racism on Japanese Twitter

### Requirements
- Install requirements using the pipenv Pipfile. 

### To load + use my pretrained Word2Vec models:
for model trained on 2015 tweet dataset: 
`w2v = gensim.models.Word2Vec.load("thesis_w2v_2015_tweets")`

for model trained on 2022 tweet dataset: 
`w2v = gensim.models.Word2Vec.load("thesis_w2v_2022_tweets")`

### To load + use my pretrained LDA (Latent Dirichlet Allocation) model:
`lda = gensim.models.LdaModel.load("thesis_lda_model_2022")`
