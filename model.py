import os
import pandas as pd

# Absolute path of this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Correct CSV path (NO dataset folder)
csv_path = os.path.join(BASE_DIR, "movies.csv")

# Load CSV safely
df = pd.read_csv(csv_path)

def recommend(mood, country, language):
    filtered = df.copy()

    if mood:
        filtered = filtered[filtered.iloc[:, 1] == mood]

    if country:
        filtered = filtered[filtered.iloc[:, 2] == country]

    if language:
        filtered = filtered[filtered.iloc[:, 3] == language]

    return filtered.to_dict(orient="records")
