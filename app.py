import streamlit as st
import pandas as pd
from recommender import get_recommendations

movies = pd.read_csv("movies.csv")

st.title("🎬 Movie Recommendation System")

option = st.radio(
    "Choose Recommendation Type",
    ["By Movie Name", "By Genre"]
)

if option == "By Movie Name":
    movie_name = st.text_input("Enter Movie Name")

    if st.button("Recommend"):
        result = get_recommendations(movie_name)

        if result is None:
            st.error("Movie not found!")
        else:
            st.write(result)

else:
    genres = movies["genre"].unique()
    selected_genre = st.selectbox("Select Genre", genres)

    if st.button("Show Movies"):
        result = movies[movies["genre"] == selected_genre]

        for _, row in result.iterrows():
            st.write(f"🎥 {row['title']} ({row['year']})")
