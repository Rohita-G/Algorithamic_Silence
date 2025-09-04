# Emotion (Motion) Analysis for Hamlet Characters
# Program Name: hamlet_emotion_analysis_textblob.py

import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob

# -----------------------------
# Step 1: Load Data
# -----------------------------
df = pd.read_csv("../data/hamlet_main_characters.csv")

# Filter main characters
main_chars = ['OPHELIA', 'HAMLET', 'GERTRUDE', 'CLAUDIUS', 'POLONIUS', 'LAERTES', 'HORATIO']
df = df[df['character'].isin(main_chars)].copy()

# -----------------------------
# Step 2: Simple Emotion Classification using TextBlob
# -----------------------------
def classify_emotion(line):
    line = str(line)
    polarity = TextBlob(line).sentiment.polarity  # -1 (negative) to +1 (positive)
    
    if polarity > 0.2:
        return 'joy'
    elif polarity < -0.2:
        return 'sadness'
    else:
        return 'neutral'

df['emotion'] = df['line'].apply(classify_emotion)

# -----------------------------
# Step 3: Aggregate Emotions per Character
# -----------------------------
emotion_counts = df.groupby(['character', 'emotion']).size().unstack(fill_value=0)

# Normalize to proportion of lines per character
emotion_prop = emotion_counts.div(emotion_counts.sum(axis=1), axis=0)

# -----------------------------
# Step 4: Visualization
# -----------------------------
plt.figure(figsize=(10, 6))
emotion_prop.plot(kind='bar', stacked=True, colormap='Pastel1', width=0.8)
plt.title("Emotion Distribution Across Main Characters in Hamlet (TextBlob)", fontsize=14, fontweight='bold')
plt.ylabel("Proportion of Lines", fontsize=12)
plt.xlabel("Character", fontsize=12)
plt.xticks(rotation=45)
plt.legend(title="Emotion", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Save figure
plt.savefig("../output/hamlet_emotion_distribution_textblob.png", dpi=300)
plt.show()

# -----------------------------
# Step 5: Optional Terminal Output
# -----------------------------
print("Emotion Counts per Character:\n", emotion_counts)
print("\nEmotion Proportion per Character:\n", emotion_prop)
