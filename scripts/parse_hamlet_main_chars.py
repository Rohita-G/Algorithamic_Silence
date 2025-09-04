# parse_hamlet_main_chars.py

import re
import pandas as pd

# --- Paths ---
hamlet_path = "../data/hamlet.txt"
output_csv = "../data/hamlet_main_characters.csv"

# --- Main characters mapping ---
# Any variant name maps to canonical name
main_chars = {
    "HAMLET": "HAMLET",
    "PRINCE": "HAMLET",
    "OPHELIA": "OPHELIA",
    "OPH.": "OPHELIA",
    "QUEEN": "QUEEN GERTRUDE",
    "QUEEN GERTRUDE": "QUEEN GERTRUDE",
    "KING": "KING CLAUDIUS",
    "KING CLAUDIUS": "KING CLAUDIUS",
    "POLONIUS": "POLONIUS",
    "LAERTES": "LAERTES",
    "HORATIO": "HORATIO"
}

# --- Read text ---
with open(hamlet_path, "r", encoding="utf-8") as f:
    text = f.read()

# --- Remove stage directions ---
text_clean = re.sub(r'\[.*?\]', '', text, flags=re.DOTALL)
text_clean = text_clean.replace('\r', '\n')

# --- Split into lines ---
lines = text_clean.split('\n')

# --- Regex for acts and scenes ---
act_pattern = re.compile(r'ACT\s+([IVXLC1-9]+)', re.IGNORECASE)
scene_pattern = re.compile(r'SCENE\s+([IVXLC1-9]+)', re.IGNORECASE)

# --- Initialize ---
data = []
current_act = None
current_scene = None
current_speaker = None
current_dialogue = []

# --- Parsing loop ---
for line in lines:
    line = line.strip()
    if not line:
        continue

    # Detect Act
    act_match = act_pattern.match(line)
    if act_match:
        current_act = act_match.group(1)
        current_scene = None
        continue

    # Detect Scene
    scene_match = scene_pattern.match(line)
    if scene_match:
        current_scene = scene_match.group(1)
        continue

    # Detect possible speaker (uppercase first word)
    words = line.split()
    if not words:
        continue
    first_word = re.sub(r'[^A-Z]', '', words[0].upper())  # clean punctuation
    if first_word in main_chars:
        speaker_name = main_chars[first_word]

        # Save previous dialogue
        if current_speaker and current_dialogue:
            dialogue_text = ' '.join(current_dialogue).strip()
            if dialogue_text:
                data.append({
                    "act": current_act,
                    "scene": current_scene,
                    "character": current_speaker,
                    "line": dialogue_text,
                    "word_count": len(dialogue_text.split())
                })

        # Start new speaker
        current_speaker = speaker_name
        remaining = ' '.join(words[1:]).strip()
        current_dialogue = [remaining] if remaining else []
    else:
        # Continue current speaker
        if current_speaker:
            current_dialogue.append(line)

# --- Save last dialogue ---
if current_speaker and current_dialogue:
    dialogue_text = ' '.join(current_dialogue).strip()
    if dialogue_text:
        data.append({
            "act": current_act,
            "scene": current_scene,
            "character": current_speaker,
            "line": dialogue_text,
            "word_count": len(dialogue_text.split())
        })

# --- Convert to DataFrame and save ---
df = pd.DataFrame(data)
df.to_csv(output_csv, index=False)
print(f"CSV saved to {output_csv}, total rows: {len(df)}")
print(df.head(10))
