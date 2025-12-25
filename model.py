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
        movie_title = str(row.iloc[0]).strip()
        movie_mood = str(row.iloc[1]).strip().lower()
        movie_country = str(row.iloc[2]).strip().lower()
        movie_language = str(row.iloc[3]).strip().lower()

        if mood and movie_mood != mood.lower():
            continue
        if country and movie_country != country.lower():
            continue
        if language and movie_language != language.lower():
            continue

        results.append({
            "title": movie_title
        })

    return results


