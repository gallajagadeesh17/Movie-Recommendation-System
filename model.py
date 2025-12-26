import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "movies.csv")

df = pd.read_csv(CSV_PATH)

def recommend(mood, country, language):
    filtered = df[
        (df["mood"] == mood) &
        (df["country"] == country) &
        (df["language"] == language)
    ]

    results = []
    for _, row in filtered.iterrows():
        results.append({
            "title": row["title"]
        })

    return results
