import os
import pickle
import streamlit as st
import requests
import gdown

# Function to fetch poster from TMDB (as you already have)
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
        data = requests.get(url).json()
        poster_path = data.get('poster_path')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
    except Exception as e:
        print("Poster fetch error:", e)
    return "https://via.placeholder.com/300x450?text=No+Poster"

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(f"https://via.placeholder.com/300x450?text={movies.iloc[i[0]].title.replace(' ', '+')}")
    return recommended_movie_names, recommended_movie_posters

st.header('🎬 Movie Recommender System')

# Load movies.pkl (assumed small enough to bundle)
movies = pickle.load(open('movies.pkl', 'rb'))

# Check & download similarity.pkl if not present
similarity_path = 'similarity.pkl'
if not os.path.exists(similarity_path):
    gd_url = 'https://drive.google.com/uc?id=1BeHE7GDGYvX2JTYE10oY9Nb32_gGDyU5&export=download'
    st.info("Downloading similarity matrix, please wait...")
    gdown.download(gd_url, similarity_path, quiet=False)
    st.success("Download complete.")

# Load similarity matrix
similarity = pickle.load(open(similarity_path, 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox("🎥 Type or select a movie from the dropdown", movie_list)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.text(recommended_movie_names[idx])
            st.image(recommended_movie_posters[idx])
