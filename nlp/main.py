import numpy as np
import matplotlib.pyplot as plt

sentence = "Attention helps models understand context."
tokens = sentence.split()

attention = [
    [0.25, 0.15, 0.20, 0.20, 0.20],
    [0.10, 0.40, 0.15, 0.20, 0.15],
    [0.15, 0.10, 0.35, 0.20, 0.20],
    [0.20, 0.15, 0.20, 0.25, 0.20],
    [0.15, 0.20, 0.20, 0.20, 0.25],
]

attention = np.array(attention)

fig, ax = plt.subplots(figsize=(8, 6))
im = ax.imshow(attention, cmap="viridis")

ax.set_xticks(np.arange(len(tokens)))
ax.set_yticks(np.arange(len(tokens)))
ax.set_xticklabels(tokens, rotation=45, ha="right")
ax.set_yticklabels(tokens)

cbar = plt.colorbar(im, ax=ax)
cbar.set_label("Attention Weight")

ax.set_title("Attention Heatmap")
ax.set_xlabel("Key Tokens")
ax.set_ylabel("Query Tokens")

plt.tight_layout()
plt.show()
