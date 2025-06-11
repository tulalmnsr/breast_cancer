
import pandas as pd
from collections import Counter
from math import log2

df = pd.read_csv("breast_cancer_clean.csv")

def calculate_entropy(data):
    label_counts = Counter(data)
    total = len(data)
    return -sum((count / total) * log2(count / total) for count in label_counts.values() if count > 0)

def information_gain(df, target_col):
    base_entropy = calculate_entropy(df[target_col])
    gains = {}
    for col in df.columns:
        if col == target_col:
            continue
        values = df[col].dropna().unique()
        weighted_entropy = 0
        for val in values:
            subset = df[df[col] == val][target_col]
            weighted_entropy += (len(subset) / len(df)) * calculate_entropy(subset)
        gains[col] = base_entropy - weighted_entropy
    return gains, base_entropy

df['Class'] = df['Class'].astype(str)
gains, entropy = information_gain(df, 'Class')
best_attr = max(gains, key=gains.get)
print(f"Dataset Entropy: {entropy}")
print(f"Best Attribute: {best_attr} with Gain: {gains[best_attr]}")
