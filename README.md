## Deconstructing “Japanese-ness”: Analyzing Perceptions of Japan's Ethnic Minorities on Twitter Using Natural Language Processing
The code for my Princeton University senior thesis research, conducted under the supervision of Dr. Christiane Fellbaum and written in fulfillment of my degree in Computer Science and minor in Japanese Language and Culture.

### Requirements
- Install requirements using the pipenv Pipfile. 

### Pretrained Word2Vec models:
To load model trained on general 2015 tweet dataset: `w2v = gensim.models.Word2Vec.load("saved_w2v_models/thesis_w2v_[YEAR]")`
- Available years: 2015, 2022

### Pretrained LDA (Latent Dirichlet Allocation) models:
To load model trained on tweets containing keyword: `lda = gensim.models.LdaModel.load("saved_lda_models/lda_model_[KEYWORD]_[YEAR]")`
- Available keywords: "zainichi" (在日コリアン), "ainu" (アイヌ), "okinawa" (沖縄人), "ryukyujin" (琉球人), "haafu" (ハーフ), "vietnamjin" (ベトナム人), "philippinejin" (フィリピン人)
- Available years: 2015, 2022
