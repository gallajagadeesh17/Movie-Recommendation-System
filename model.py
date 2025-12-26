import os
import pandas as pd

# Get base directory of this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# CSV file path (must be in same folder as model.py)
CSV_PATH = os.path.join(BASE_DIR, "movies.csv")

# 🔍 DEBUG (VERY IMPORTANT)
print("CSV PATH:", CSV_PATH)
print("CSV EXISTS:", os.path.exists(CSV_PATH))

# Load CSV
df = pd.read_csv(CSV_PATH)

def recommend(mood, country, language):
    # Make a safe copy
    temp_df = df.copy()

    # Normalize CSV values
    temp_df["mood"] = temp_df["mood"].astype(str).str.strip().str.lower()
    temp_df["country"] = temp_df["country"].astype(str).str.strip().str.lower()
    temp_df["language"] = temp_df["language"].astype(str).str.strip().str.lower()

    # Normalize form inputs
    mood = mood.strip().lower()
    country = country.strip().lower()
    language = language.strip().lower()

    # Filter data
    filtered = temp_df[
        (temp_df["mood"] == mood) &
        (temp_df["country"] == country) &
        (temp_df["language"] == language)
    ]

    # 🔍 DEBUG
    print("FILTERED ROWS:", len(filtered))

    results = []
    for _, row in filtered.iterrows():
        results.append({
            "title": row["title"]
        })

    return results
