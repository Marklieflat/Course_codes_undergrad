import numpy as np
import pandas as pd
import nltk
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from wordcloud import WordCloud
from readability import Readability

# Q1
def transfer_to_pos(df):
    if df['Tag'].startswith('J'):
        df['Pos'] = 'a'
    elif df['Tag'].startswith('V'):
        df['Pos'] = 'v'
    elif df['Tag'].startswith('N'):
        df['Pos'] = 'n'
    elif df['Tag'].startswith('R'):
        df['Pos'] = 'r'
    else:
        df['Pos'] = 'x'
    return df

article_str = """
Tesla's third-quarter sales jumped 44%\ as
global demand for its electric vehicles outpaced 
that of most other automakers. The company reported
Friday that it had delivered 139,000 SUVs and sedans
from July through September, compared with 97,000
deliveries during the same period a year ago. The
sales topped even some of the most optimistic projections
coming from Wall Street. Analysts polled by data provider
FactSet expected the company to sell closer to 137,000.
Tesla has been rewriting the script throughout the year
amidst a pandemic that has closed factories and scrambled
supply lines. This puts Musk & Co. in prime position to
hit the area code of 500k units for the year which six months
ago was not even on the map for the bulls, Daniel Ives of
Wedbush wrote Friday. China was likely a major source of
strength in the quarter, Ives said. Tesla could post its fifth
consecutive quarter of profits later this month.
"""
words_list = word_tokenize(article_str)
words_tags = nltk.pos_tag(words_list)
words_tags_df = pd.DataFrame(words_tags, columns=['Word_original', 'Tag'])
words_tags_df = words_tags_df.apply(transfer_to_pos, axis=1)
words_tags_df = words_tags_df[words_tags_df['Pos'] != 'x']
words_tags_df = words_tags_df.reset_index(drop=True)
words_tags_df['words_lemmatized'] = words_tags_df.apply(lambda x: WordNetLemmatizer().lemmatize(x['Word_original'], pos=x['Pos']), axis=1)
lemmatized_list = words_tags_df['words_lemmatized'].tolist()
lemmatized_str = ' '.join(lemmatized_list)
wordcloud = WordCloud(width = 1000, height = 700, background_color = 'black', stopwords = 'set', min_font_size = 10).generate(lemmatized_str)
plt.figure(figsize=(10, 7), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()

# Q2
pos_words_list = pd.read_excel('LoughranMcDonald_SentimentWordLists_2018.xlsx', sheet_name='Positive', header=None)
neg_words_list = pd.read_excel('LoughranMcDonald_SentimentWordLists_2018.xlsx', sheet_name='Negative', header=None)

def judge_sentiment(df):
    if df['words_lemmatized'].upper() in pos_words_list[0].tolist():
        df['sentiment'] = 1
    elif df['words_lemmatized'].upper() in neg_words_list[0].tolist():
        df['sentiment'] = -1
    else:
        df['sentiment'] = 0
    return df

words_tags_df = words_tags_df.apply(judge_sentiment, axis=1)
num = words_tags_df['sentiment'].sum()
denom = len(words_tags_df)
new_sentiment = num / denom
print(new_sentiment)

# Q3. Calculate the Fog Index using py-readability-metrics
r = Readability(article_str)
fog_index = r.gunning_fog().score
print(fog_index)

# Q4
tesla_data = pd.read_excel('FIN3210 Week 5 Tesla.xlsx')
summary_stat_data = tesla_data[['Sentiment','Novelty','Impact']]
summary_stat = summary_stat_data.describe()
print(summary_stat)
print(summary_stat_data.corr())

news_categories = tesla_data['Category'].value_counts().reset_index()
news_categories.columns = ['Category', 'Frequency']
news_categories['Fractions'] = news_categories['Frequency'] / news_categories['Frequency'].sum()
print(news_categories[:10])