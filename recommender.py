import pandas as pd

def load_data():
    return pd.read_csv("movies.csv")

def get_recommendations(movie_name):
    df = load_data()

    movie = df[df["title"].str.lower() == movie_name.lower()]

    if movie.empty:
        return None

    genre = movie.iloc[0]["genre"]

    recommendations = df[
        (df["genre"] == genre) &
        (df["title"].str.lower() != movie_name.lower())
    ]

    result = []

    for _, row in recommendations.iterrows():
        result.append(
            f"{row['title']} ({row['year']}) - {row['genre']}"
        )

    return result[:5]