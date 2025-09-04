# extract_ophelia.py

import pandas as pd

# Paths
input_csv = "../data/hamlet_main_characters.csv"
output_csv = "../data/hamlet_ophelia_lines.csv"

# Load main characters CSV
df = pd.read_csv(input_csv)

# Filter Ophelia
df_ophelia = df[df['character'] == 'OPHELIA']

# Save Ophelia lines
df_ophelia.to_csv(output_csv, index=False)
print(f"Ophelia CSV saved to {output_csv}, total rows: {len(df_ophelia)}")
print(df_ophelia.head())

# Word count per act
word_counts = df_ophelia.groupby('act')['word_count'].sum()
print("Ophelia word count per act:\n", word_counts)

# Dialogue count per act
line_counts = df_ophelia.groupby('act').size()
print("Ophelia lines per act:\n", line_counts)

# Percentage of total main character dialogue
total_words = df['word_count'].sum()
ophelia_words = df_ophelia['word_count'].sum()
percentage = (ophelia_words / total_words) * 100
print(f"Ophelia speaks {percentage:.2f}% of all main character words")

# Total words spoken by all main characters
total_words = df['word_count'].sum()
print(f"Total words spoken by main characters: {total_words}")
