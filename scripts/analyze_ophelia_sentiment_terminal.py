# analyze_ophelia_sentiment_terminal.py

import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Download VADER lexicon
nltk.download('vader_lexicon')

# Paths
input_csv = "../data/hamlet_main_characters.csv"

# Load main characters CSV
df = pd.read_csv(input_csv)

# Filter main characters
main_chars = ['OPHELIA', 'HAMLET', 'GERTRUDE', 'CLAUDIUS', 'POLONIUS', 'LAERTES', 'HORATIO']
df = df[df['character'].isin(main_chars)]

# Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Compute sentiment per line
df['compound'] = df['line'].apply(lambda x: sia.polarity_scores(str(x))['compound'])

# --- Act-level sentiment summary ---
act_sent = df.groupby(['act', 'character'])['compound'].agg(['mean','min','max']).reset_index()

print("\n--- Act-Level Sentiment Summary ---")
for act in sorted(df['act'].unique()):
    print(f"\nACT {act}")
    subset = act_sent[act_sent['act']==act]
    for _, row in subset.iterrows():
        print(f"{row['character']}: mean={row['mean']:.3f}, min={row['min']:.3f}, max={row['max']:.3f}")

# --- Scene-level sentiment for Ophelia ---
ophelia_df = df[df['character']=='OPHELIA']
scene_sent = ophelia_df.groupby(['act','scene'])['compound'].mean().reset_index()

print("\n--- Ophelia Scene-Level Sentiment ---")
for _, row in scene_sent.iterrows():
    print(f"Act {row['act']}, Scene {row['scene']}: avg_compound={row['compound']:.3f}")

# --- Overall stats ---
ophelia_total_words = ophelia_df['word_count'].sum()
total_words = df['word_count'].sum()
percentage = (ophelia_total_words / total_words) * 100
print(f"\nOphelia total words: {ophelia_total_words} ({percentage:.2f}% of main character dialogue)")

ophelia_mean_sent = ophelia_df['compound'].mean()
print(f"Ophelia average sentiment (compound) across all lines: {ophelia_mean_sent:.3f}")
