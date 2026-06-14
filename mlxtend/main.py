import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

def extract_top_lift_rules(df, min_support=0.2, min_confidence=0.5, top_n=3):
    frequent_itemsets = apriori(df, min_support=min_support, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
    filtered_rules = rules[rules['confidence'] >= min_confidence]
    sorted_rules = filtered_rules.sort_values(by='lift', ascending=False)
    top_rules = sorted_rules.head(top_n)
    return top_rules

# Sample transaction data (one-hot encoded)
data = {
    'milk':   [1, 0, 0, 1, 1],
    'bread':  [1, 1, 0, 1, 0],
    'eggs':   [0, 1, 1, 1, 0],
    'butter': [0, 0, 1, 1, 1],
}
df = pd.DataFrame(data)

result = extract_top_lift_rules(df, min_support=0.2, min_confidence=0.5, top_n=2)
print(result)