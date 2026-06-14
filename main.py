import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def customers_also_bought(transactions, item_id, top_n=3):
    # Build item-user matrix
    item_user_matrix = pd.crosstab(transactions['item_id'], transactions['user_id'])
    # Compute cosine similarity between items
    similarity = cosine_similarity(item_user_matrix)
    similarity_df = pd.DataFrame(similarity, index=item_user_matrix.index, columns=item_user_matrix.index)
    # Remove self-similarity
    similarity_df.loc[item_id, item_id] = 0
    # Prepare a DataFrame for sorting by similarity and item_id as tiebreaker
    sim_series = similarity_df.loc[item_id]
    sim_df = sim_series.reset_index()
    sim_df.columns = ['item_id', 'similarity']
    # Remove the target item
    sim_df = sim_df[sim_df['item_id'] != item_id]
    # Sort by similarity descending, then item_id lex descending for deterministic output
    sim_df = sim_df.sort_values(['similarity', 'item_id'], ascending=[False, False])
    # Select up to top_n items
    top_items = sim_df['item_id'].head(top_n).tolist()
    return top_items

transactions = pd.DataFrame({
    "user_id": [1, 2, 1, 3, 2, 3, 4, 4, 1],
    "item_id": ["apple", "banana", "banana", "apple", "carrot", "carrot", "apple", "banana", "carrot"]
})
result = customers_also_bought(transactions, "apple", top_n=2)
print(result)
