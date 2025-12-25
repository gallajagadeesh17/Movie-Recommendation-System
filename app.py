import streamlit as st
import pandas as pd

df = pd.read_csv("movies.csv")

st.title("🎬 Movie Recommendation System")

mood = st.selectbox("Select Mood", sorted(df["mood"].unique()))
country = st.selectbox("Select Country", sorted(df["country"].unique()))
language = st.selectbox("Select Language", sorted(df["language"].unique()))

if st.button("Recommend"):
    result = df[
        (df["mood"] == mood) &
        (df["country"] == country) &
        (df["language"] == language)
    ]

    if result.empty:
        st.warning("No movies found")
    else:
        for movie in result["title"]:
            st.success(movie)
