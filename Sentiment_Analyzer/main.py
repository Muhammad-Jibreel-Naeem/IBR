from newspaper import Article
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

url = input('Enter a URL: ')

article = Article(url)
article.download()
article.parse()

analyzer = SentimentIntensityAnalyzer()
scores = analyzer.polarity_scores(article.text)

compound = scores['compound']

# Determine tone
if compound >= 0.05:
    tone = "positive"
elif compound <= -0.05:
    tone = "negative"
else:
    tone = "neutral"

abs_compound = abs(compound)
if abs_compound >= 0.7:
    opinion_level = "strongly opinionated"
elif abs_compound >= 0.4:
    opinion_level = "moderately opinionated"
elif abs_compound >= 0.1:
    opinion_level = "slightly opinionated"
else:
    opinion_level = "mostly neutral or factual"

print(f"The article has a {tone} tone and is {opinion_level}.")

# Optional: Visual display
fig, ax = plt.subplots()
ax.axis('off')
ax.text(0.5, 1, f'Title: {article.title}', fontsize=7, ha='center', va='center')
ax.text(0.5, 0.5, f'Tone: {tone.capitalize()}\nOpinion Level: {opinion_level.capitalize()}', fontsize=12, ha='center', va='center')
plt.show()
