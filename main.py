import numpy as np
import pandas as pd
from numpy.linalg import norm

def recommend_products(user_item_matrix, target_user, top_n=3):
    target_vector = user_item_matrix.loc[target_user].values
    similarities = {}
    for user in user_item_matrix.index:
        if user == target_user:
            continue
        user_vector = user_item_matrix.loc[user].values
        if norm(target_vector) == 0 or norm(user_vector) == 0:
            sim = 0.0
        else:
            sim = np.dot(target_vector, user_vector) / (norm(target_vector) * norm(user_vector))
        similarities[user] = sim

    if not similarities:
        return []
    max_sim = max(similarities.values())
    if max_sim == 0:
        return []
    most_similar_user = max(similarities, key=similarities.get)
    similar_user_items = user_item_matrix.loc[most_similar_user]
    target_user_items = user_item_matrix.loc[target_user]
    recommendable_items = similar_user_items[(similar_user_items > 0) & (target_user_items == 0)]
    if recommendable_items.empty:
        return []
    recommendations = recommendable_items.sort_values(ascending=False).head(top_n).index.tolist()
    return recommendations

data = {
    'apple': [1, 0, 1, 0],
    'banana': [1, 1, 0, 0],
    'carrot': [0, 1, 1, 0],
    'donut': [0, 0, 1, 1],
}
user_item_matrix = pd.DataFrame(data, index=['alice', 'bob', 'carol', 'dave'])

result = recommend_products(user_item_matrix, 'bob', top_n=2)
print(result)
