import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations

# Load main characters CSV
df = pd.read_csv("../data/hamlet_main_characters.csv")
main_chars = ['OPHELIA', 'HAMLET', 'GERTRUDE', 'CLAUDIUS', 'POLONIUS', 'LAERTES', 'HORATIO']
df = df[df['character'].isin(main_chars)]

# Co-occurrence
co_occurrence = {}
for (act, scene), group in df.groupby(['act','scene']):
    chars_in_scene = group['character'].unique()
    for pair in combinations(chars_in_scene, 2):
        pair = tuple(sorted(pair))
        co_occurrence[pair] = co_occurrence.get(pair, 0) + 1

# Create graph
G = nx.Graph()
for char in main_chars:
    word_count = df[df['character']==char]['word_count'].sum()
    # Normalize node size
    size = max(500, min(word_count, 2000))
    G.add_node(char, size=size)

for (c1,c2), weight in co_occurrence.items():
    # Normalize edge weight
    G.add_edge(c1,c2, weight=max(1, weight))

# Layout
pos = nx.kamada_kawai_layout(G)

# Node size and color
sizes = [G.nodes[n]['size'] for n in G.nodes()]
colors = ['red' if n=='OPHELIA' else 'skyblue' for n in G.nodes()]

# Edge width
edges = [G[u][v]['weight'] for u,v in G.edges()]

# Draw graph
plt.figure(figsize=(10,8))
nx.draw_networkx_nodes(G, pos, node_size=sizes, node_color=colors, alpha=0.9)
nx.draw_networkx_edges(G, pos, width=edges, alpha=0.5)
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

# Draw edge labels (co-occurrence counts)
edge_labels = {(u,v): G[u][v]['weight'] for u,v in G.edges()}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

plt.title("Hamlet: Main Character Network (Scene Co-occurrence)")
plt.axis('off')
plt.tight_layout()
plt.savefig("../output/hamlet_character_network_clean_labels.png", dpi=300)
plt.show()
