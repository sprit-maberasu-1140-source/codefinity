# Calculate evaluation metrics for a binary text classifier.
# Fill in the variables below with your calculated values, rounded to two decimal places.

# True values: 6 positive, 4 negative
# Model predictions: 5 positive (4 correct), 5 negative (3 correct)

# Confusion matrix for positive class:
# True Positives (TP): 4 (predicted positive and actually positive)
# False Positives (FP): 1 (predicted positive but actually negative)
# False Negatives (FN): 2 (predicted negative but actually positive)
# True Negatives (TN): 3 (predicted negative and actually negative)

accuracy = 0.7  # (TP + TN) / total = (4 + 3) / 10 = 0.7
precision = 0.8  # TP / (TP + FP) = 4 / (4 + 1) = 0.8
recall = 0.67  # TP / (TP + FN) = 4 / (4 + 2) ≈ 0.666..., rounded to 0.67
f1_score = 0.73  # 2 * (precision * recall) / (precision + recall) = 2 * (0.8 * 0.67) / (0.8 + 0.67) ≈ 0.727..., rounded to 0.73
