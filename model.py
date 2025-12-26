import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "movies.csv")

df = pd.read_csv(CSV_PATH)

def recommend(mood, country, language):
    # make a COPY so original df is untouched
    temp_df = df.copy()

    # normalize CSV values
    temp_df["mood"] = temp_df["mood"].astype(str).str.strip().str.lower()
    temp_df["country"] = temp_df["country"].astype(str).str.strip().str.lower()
    temp_df["language"] = temp_df["language"].astype(str).str.strip().str.lower()

    # normalize form input
    mood = mood.strip().lower()
    country = country.strip().lower()
    language = language.strip().lower()

    filtered = temp_df[
        (temp_df["mood"] == mood) &
        (temp_df["country"] == country) &
        (temp_df["language"] == language)
    ]

    results = []
    for _, row in filtered.iterrows():
        results.append({
            "title": row["title"]
        })

    return results
