import os
import pandas as pd

# Absolute path of this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Correct CSV path (NO dataset folder)
csv_path = os.path.join(BASE_DIR, "movies.csv")

# Load CSV safely
df = pd.read_csv(csv_path)

def recommend(mood, country, language):
    results = []

    for _, row in df.iterrows():
        results.append({
            "title": str(row.iloc[0])
        })

    return results



