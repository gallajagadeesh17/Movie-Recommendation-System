import pandas as pd

# Load dataset
movies = pd.read_csv("dataset/movies.csv", encoding="latin1")

# Fix hidden BOM characters from Excel
movies.columns = movies.columns.str.replace('ï»¿', '').str.strip()

def recommend(mood, country, language):
    result = movies[
        (movies['mood'] == mood) &
        (movies['country'] == country) &
        (movies['language'] == language)
    ]

    return result['title'].tolist()
