import numpy as np

def evaluate_predictions(predicted_ratings, actual_ratings):
    predicted_ratings_np = np.array(predicted_ratings)
    actual_ratings_np = np.array(actual_ratings)
    # MSE over all items
    mse = np.mean((predicted_ratings_np - actual_ratings_np) ** 2)
    # Top 3 predicted item indices
    top3_pred_indices = np.argsort(predicted_ratings_np)[::-1][:3]
    # Precision at 3: overlap of top 3 predicted items with top 3 actual items
    top3_actual_indices = np.argsort(actual_ratings_np)[::-1][:3]
    precision_at_3 = len(set(top3_pred_indices) & set(top3_actual_indices)) / 3
    return mse, precision_at_3

predicted_ratings = [2.5, 4.0, 3.5, 5.0, 1.0]
actual_ratings = [3.0, 5.0, 2.0, 4.0, 1.0]
mse, precision_at_3 = evaluate_predictions(predicted_ratings, actual_ratings)
result_mse = mse
result_precision_at_3 = precision_at_3
print("MSE:", result_mse)
print("Precision@3:", result_precision_at_3)
