# analyze_ophelia_sentiment.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# --- Download VADER lexicon ---
nltk.download('vader_lexicon')

# --- Paths ---
input_csv = "../data/hamlet_main_characters.csv"
output_csv = "../data/hamlet_sentiment.csv"

# --- Load main characters CSV ---
df = pd.read_csv(input_csv)

# Filter only main characters
main_chars = ['OPHELIA', 'HAMLET', 'GERTRUDE', 'CLAUDIUS', 'POLONIUS', 'LAERTES', 'HORATIO']
df = df[df['character'].isin(main_chars)]

# --- Initialize sentiment analyzer ---
sia = SentimentIntensityAnalyzer()

# --- Compute sentiment per line ---
sentiments = df['line'].apply(lambda x: sia.polarity_scores(str(x)))
sent_df = pd.DataFrame(list(sentiments))
df = pd.concat([df.reset_index(drop=True), sent_df], axis=1)

# --- Save beat-level sentiment CSV ---
df.to_csv(output_csv, index=False)
print(f"Beat-level sentiment CSV saved to {output_csv}, total rows: {len(df)}")

# --- Aggregate sentiment per act ---
act_sentiment = df.groupby(['act', 'character'])['compound'].mean().reset_index()

# --- Visualization 1: Act-by-Act Compound Sentiment ---
plt.figure(figsize=(10,6))
sns.lineplot(data=act_sentiment, x='act', y='compound', hue='character', marker='o')
plt.title("Act-by-Act Average Sentiment (Compound) by Character")
plt.xlabel("Act")
plt.ylabel("Average Compound Sentiment")
plt.legend(title='Character')
plt.tight_layout()
plt.savefig("../output/act_sentiment_by_character.png")  # Save figure
plt.close()

# --- Scene-level heatmap for Ophelia ---
ophelia_df = df[df['character'] == 'OPHELIA']
scene_sentiment = ophelia_df.groupby(['act','scene'])['compound'].mean().unstack(fill_value=0)

plt.figure(figsize=(12,4))
sns.heatmap(scene_sentiment, annot=True, cmap="coolwarm", center=0)
plt.title("Ophelia: Scene-level Compound Sentiment")
plt.xlabel("Scene")
plt.ylabel("Act")
plt.tight_layout()
plt.savefig("../output/ophelia_scene_sentiment.png")  # Save figure
plt.close()

# --- Histogram of sentiment distribution ---
plt.figure(figsize=(10,6))
sns.histplot(data=df, x='compound', hue='character', multiple='stack', bins=20)
plt.title("Distribution of Line Sentiment by Character")
plt.xlabel("Compound Sentiment")
plt.ylabel("Number of Lines")
plt.tight_layout()
plt.savefig("../output/sentiment_distribution.png")  # Save figure
plt.close()
