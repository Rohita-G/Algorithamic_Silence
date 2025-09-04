# visualize_ophelia.py

import pandas as pd
import matplotlib.pyplot as plt

# --- Paths ---
input_csv = "../data/hamlet_ophelia_lines.csv"

# --- Load Ophelia lines ---
df_ophelia = pd.read_csv(input_csv)

# --- Word count per act ---
word_counts = df_ophelia.groupby('act')['word_count'].sum()

# --- Plot ---
plt.figure(figsize=(8,5))
word_counts.plot(kind='bar', color='pink')
plt.title("Ophelia's Word Count per Act")
plt.xlabel("Act")
plt.ylabel("Total Words")
plt.xticks(rotation=0)
plt.tight_layout()

# --- Save figure ---
plt.savefig("../output/ophelia_word_count_per_act.png")
plt.show()

# --- Print summary ---
print("Ophelia word count per act:\n", word_counts)
print(f"Total words spoken by Ophelia: {word_counts.sum()}")
