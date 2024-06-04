## Deconstructing “Japanese-ness”: Analyzing Perceptions of Japan's Ethnic Minorities on Twitter Using Natural Language Processing
The code for my Princeton University senior thesis research, conducted under the supervision of Dr. Christiane Fellbaum and written in fulfillment of my degree in Computer Science and minor in Japanese Language and Culture.
 
**Abstract:** _This study analyzes Japanese tweets via natural language processing techniques, in order to provide insight into current perceptions of ethnic minorities in Japan. While existing work has studied different topics on Japanese Twitter or researched online racism in other countries, most studies rely on manual labeling and purely qualitative analysis, and none have studied online racial discrimination in a Japanese context. Drawing on the existing sociological literature, this research fills this gap by introduc- ing a rigorous quantitative component to the study of Japan’s minorities, applying Word2Vec semantic vector similarity analysis and Latent Dirichlet Allocation (LDA) analysis to sixteen total tweet datasets. By studying changes over time in common topics and keywords associated with different minority groups, this work compares and contrasts discourse pertaining to Zainichi Koreans, native Ainu and Okinawan populations, Hāfu, and Southeast Asian migrants, in order to develop a broadened understanding of racial discrimination and attitudes toward minorities in Japan to- day. The data suggest that the conversation surrounding a minority group generally reflects a level of awareness of social issues that corresponds to the group’s history of advocacy efforts and established presence in Japan._

### Guide
- `thesis_twscrape.ipynb`: code for scraping Tweets
- `thesis_preprocess.ipynb`: code for preprocessing Tweets
- `thesis_w2v.ipynb`: code for running Word2Vec analysis
- `thesis_lda.ipynb`: code for running LDA analysis
- `thesis_lda_run.ipynb`: runs code in `thesis_lda_run.ipynb` on all minority keyword datasets

### Requirements
- Install requirements using the pipenv Pipfile.

### Pretrained Word2Vec Models
To load model trained on general tweet dataset: `w2v = gensim.models.Word2Vec.load("saved_w2v_models/thesis_w2v_[YEAR]")`
- Available years: 2015, 2022

### Pretrained LDA (Latent Dirichlet Allocation) Models
To load model trained on minority keyword tweet dataset: `lda = gensim.models.LdaModel.load("saved_lda_models/lda_model_[KEYWORD]_[YEAR]")`
- Available keywords: "zainichi" (在日コリアン), "ainu" (アイヌ), "okinawa" (沖縄人), "ryukyujin" (琉球人), "haafu" (ハーフ), "vietnamjin" (ベトナム人), "philippinejin" (フィリピン人)
- Available years: 2015, 2022
