## Questioning “Japanese-ness”: A Holistic Analysis of Racism on Japanese Twitter

### Requirements
- Install requirements using the pipenv Pipfile. 

### To load + use pretrained Word2Vec models:
- Model trained on general 2015 tweet dataset: `w2v = gensim.models.Word2Vec.load("saved_w2v_models/thesis_w2v_2015")`
- Model trained on general 2022 tweet dataset: `w2v = gensim.models.Word2Vec.load("saved_w2v_models/thesis_w2v_2022")`

### To load + use pretrained LDA (Latent Dirichlet Allocation) models:
- Model trained on "アイヌ" (Ainu) keyword 2022 tweet dataset: `lda = gensim.models.LdaModel.load("saved_lda_models/lda_model_ainu_2022")`
- Model trained on "ハーフ" (_Haafu_) keyword 2022 tweet dataset: `lda = gensim.models.LdaModel.load("saved_lda_models/lda_model_haafu_2022")`
- Model trained on "沖縄人" (Okinawajin) keyword 2022 tweet dataset: `lda = gensim.models.LdaModel.load("saved_lda_models/lda_model_okinawajin_2022")`
- Model trained on "琉球人" (Ryukyujin) keyword 2022 tweet dataset: `lda = gensim.models.LdaModel.load("saved_lda_models/lda_model_ryukyujin_2022")`
- Model trained on "在日コリアン" (Zainichi Korean) keyword 2022 tweet dataset: `lda = gensim.models.LdaModel.load("saved_lda_models/lda_model_zainichi_2022")`
