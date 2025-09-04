 Algorithmic Silence: Computational Analysis of *Hamlet*

This repository presents a computational study of William Shakespeare’s *Hamlet*, focusing on **Ophelia’s narrative presence and structural marginalization**. Using natural language processing, sentiment analysis, and network mapping, the project quantifies how Ophelia’s voice compares to other central characters.

---

 📌 Overview

The project combines **digital humanities** and **computational text analysis** to answer:

* How much does Ophelia speak compared to other main characters?
* What emotional tone is carried in her dialogue across acts and scenes?
* How is Ophelia structurally positioned in the play’s character network?

By integrating **word count statistics**, **sentiment trajectories**, and **co-occurrence networks**, the analysis provides new evidence for Ophelia’s silence as both **quantitative absence** and **structural marginality**.

---

 📂 Repository Structure

```
Algorithmic_Silence/
│
├── data/                    
│   ├── hamlet_main_characters.csv    Extracted character-level lines
│   ├── hamlet_ophelia_lines.csv      Ophelia-only dataset
│   └── hamlet_sentiment.csv          Sentiment-scored dialogue
│
├── scripts/                
│   ├── extract_characters.py         Parse & export main characters
│   ├── extract_ophelia.py            Isolate Ophelia’s lines
│   ├── visualize_ophelia.py          Word count analysis
│   ├── analyze_ophelia_sentiment.py  Sentiment analysis & graphs
│   └── character_network.py          Scene-level co-occurrence network
│
├── output/                  
│   ├── ophelia_wordcount.png
│   ├── ophelia_sentiment_heatmap.png
│   ├── sentiment_distribution.png
│   └── hamlet_character_network.png
│
├── requirements.txt
└── README.md
```

---

 ⚙️ Installation & Setup

 Prerequisites

* Python 3.9 or higher
* Recommended: virtual environment (`venv` or `conda`)

 Installation

```bash
git clone https://github.com/<your-username>/Algorithmic_Silence.git
cd Algorithmic_Silence
pip install -r requirements.txt
```

Dependencies include:

* **pandas** – structured text processing
* **matplotlib / seaborn** – visualization
* **nltk (VADER)** – sentiment analysis
* **networkx** – character network construction

---

 ▶️ Usage

 1. Extract main character dialogue

```bash
python scripts/extract_characters.py
```

 2. Isolate Ophelia’s speech

```bash
python scripts/extract_ophelia.py
```

 3. Word count visualizations

```bash
python scripts/visualize_ophelia.py
```

 4. Sentiment analysis

```bash
python scripts/analyze_ophelia_sentiment.py
```

 5. Character network mapping

```bash
python scripts/character_network.py
```

Outputs are saved automatically in the **`output/`** directory.

---

 📊 Results (Highlights)

* **Speech distribution**: Ophelia speaks \~1,245 words, only **4–5% of main character dialogue**.
* **Sentiment trajectory**: Negative polarity intensifies in Act 2 (avg. compound = –0.519) and does not fully recover.
* **Network centrality**: Ophelia is peripheral in the scene co-occurrence network, linked primarily through Hamlet, Polonius, and Laertes.

---

 ✍️ Academic Context

This project contributes to **algorithmic literary analysis** by quantifying Ophelia’s “algorithmic silence.”
It demonstrates how computational metrics (word counts, sentiment scoring, network mapping) can make visible patterns of **structural marginalization** often discussed qualitatively in literary criticism.

---

 📜 Citation

If you use this repository, please cite as:

> Rohita G. *Algorithmic Silence: Computational Analysis of Hamlet.* 2025.


