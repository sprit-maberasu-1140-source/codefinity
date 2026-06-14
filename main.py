import pandas as pd
from collections import Counter

def find_frequent_single_items(transactions, min_support):
    item_counts = Counter()
    for transaction in transactions:
        item_counts.update(transaction)
    result = [(item, count) for item, count in item_counts.items() if count >= min_support]
    result.sort(key=lambda x: (-x[1], x[0]))
    return result

# Sample synthetic dataset
transactions = [
    ['milk', 'bread', 'eggs'],
    ['bread', 'butter'],
    ['milk', 'bread', 'butter', 'eggs'],
    ['bread', 'eggs'],
    ['milk', 'bread', 'eggs'],
    ['butter', 'eggs'],
    ['milk', 'bread'],
    ['milk', 'eggs'],
    ['bread', 'butter'],
    ['milk', 'bread', 'eggs', 'butter']
]

min_support = 3

frequent_items = find_frequent_single_items(transactions, min_support)
print(frequent_items)