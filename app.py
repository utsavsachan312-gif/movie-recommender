import streamlit as st
from recommender import get_recommendations

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬"
)

st.title("🎬 Movie Recommendation System")

st.write("Enter a movie name and get similar recommendations.")

movie_name = st.text_input("Movie Name")

if st.button("Recommend"):

    if movie_name.strip() == "":
        st.warning("Please enter a movie name.")
    else:

        result = get_recommendations(movie_name)

        if result is None:
            st.error("Movie not found!")
        else:
            st.subheader("Recommended Movies")

            for movie in result:
                st.write("✅", movie)