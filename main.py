def calculate_association_metrics(transactions, item_a, item_b):
    total_transactions = len(transactions)
    support_ab = 0
    support_a = 0
    support_b = 0

    for transaction in transactions:
        if item_a in transaction and item_b in transaction:
            support_ab += 1
        if item_a in transaction:
            support_a += 1
        if item_b in transaction:
            support_b += 1

    support = support_ab / total_transactions
    confidence = support_ab / support_a if support_a > 0 else 0
    lift = (confidence / (support_b / total_transactions)) if support_b > 0 else 0

    result = {
        "support": support,
        "confidence": confidence,
        "lift": lift
    }
    return result

# Sample transaction ledger
transactions = [
    ["milk", "bread", "butter"],
    ["bread", "butter"],
    ["milk", "bread"],
    ["milk", "eggs"],
    ["bread", "eggs"],
    ["milk", "bread", "butter", "eggs"]
]

# Example usage
metrics_milk_bread = calculate_association_metrics(transactions, "milk", "bread")
print(metrics_milk_bread)

metrics_bread_butter = calculate_association_metrics(transactions, "bread", "butter")
print(metrics_bread_butter)
