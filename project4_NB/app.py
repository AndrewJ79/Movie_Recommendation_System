import os
import requests
import numpy as np
from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv 

app = Flask(__name__)
# Load environment variables from .env
load_dotenv()

# Fetch the API key
API_KEY = os.getenv('TMDB_API_KEY')




# Function to get movie recommendations
def get_movie_recommendations(genre=None, mood=None, popularity=False):
    base_url = "https://api.themoviedb.org/3/discover/movie"
    params = {
        "api_key": API_KEY,
        "sort_by": "popularity.desc" if popularity else "vote_average.desc",
        "vote_count.gte": 100,
        "language": "en-US"
    }
    
    if genre:
        genre_dict = {
            "action": 28,
            "comedy": 35,
            "drama": 18,
            "horror": 27,
            "sci-fi": 878,
            "romance": 10749,
            "thriller": 53
        }
        params["with_genres"] = genre_dict.get(genre.lower())
    
    if mood:
        mood_dict = {
            "happy": "35,10749",
            "sad": "18,10749",
            "exciting": "28,53",
            "dark": "27,53",
            "thoughtful": "18,878"
        }
        params["with_genres"] = mood_dict.get(mood.lower())
    
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        movies = response.json().get("results", [])
        if movies:
            return movies[:10]  # Return top 10 movies
    return None

# Function to recommend similar movies based on the description
def recommend_similar_movies(movies):
    descriptions = [movie['overview'] for movie in movies if 'overview' in movie]
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(descriptions)
    similarity_matrix = cosine_similarity(tfidf_matrix)
    
    most_similar_index = np.argmax(np.sum(similarity_matrix, axis=1))
    return movies[most_similar_index] if movies else None

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to get movie recommendations based on user input
@app.route('/recommend', methods=['POST'])
def recommend():
    genre = request.form.get('genre', '').strip().lower()
    mood = request.form.get('mood', '').strip().lower()
    popularity = request.form.get('popularity', 'false').lower() == 'true'

    movies = None
    if genre in ["action", "comedy", "drama", "horror", "sci-fi", "romance", "thriller"]:
        movies = get_movie_recommendations(genre=genre)
    elif mood in ["happy", "sad", "exciting", "dark", "thoughtful"]:
        movies = get_movie_recommendations(mood=mood)
    elif popularity:
        movies = get_movie_recommendations(popularity=True)
    
    similar_movie = None
    if movies:
        similar_movie = recommend_similar_movies(movies)
    
    return render_template('index.html', movies=movies, similar_movie=similar_movie)

if __name__ == '__main__':
    app.run(debug=True,port=5500)
