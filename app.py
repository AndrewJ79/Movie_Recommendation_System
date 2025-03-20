import os
import requests
import numpy as np
import pandas as pd
from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv('TMDB_API_KEY')

# Load the pre-saved ALS recommendations CSV file (for collaborative filtering)
recommendations_df = pd.read_csv('resources\\top_n_recommendations.csv')

# -------------------------
# CONTENT-BASED RECOMMENDATIONS
# -------------------------
def get_movie_recommendations(genre=None, mood=None, popularity=False):
    base_url = "https://api.themoviedb.org/3/discover/movie"
    params = {
        "api_key": API_KEY,
        "sort_by": "popularity.desc" if popularity else "vote_average.desc",
        "vote_count.gte": 100,
        "language": "en-US"
    }
    # Use genre if provided; otherwise, if mood is provided use that mapping
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
    elif mood:
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

def recommend_similar_movies(movies):
    # Get movie overviews; if missing, use an empty string
    descriptions = [movie.get('overview', '') for movie in movies]
    if not descriptions:
        return None
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(descriptions)
    similarity_matrix = cosine_similarity(tfidf_matrix)
    most_similar_index = np.argmax(np.sum(similarity_matrix, axis=1))
    most_similar_movie = movies[most_similar_index] if movies else None
    # Ensure genre_name exists (defaulting to 'Unknown' if not found)
    if most_similar_movie:
        most_similar_movie['genre_name'] = most_similar_movie.get('genre_name', 'Unknown')
    return most_similar_movie

# Route for Content-Based Filtering (Main Page)
@app.route('/')
@app.route('/mainpage.html')
def index():
    # Render content-based recommendations page (initially without movies)
    return render_template('mainpage.html')

# Route to get content-based recommendations
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
    return render_template('mainpage.html', movies=movies, similar_movie=similar_movie)

# -------------------------
# COLLABORATIVE FILTERING RECOMMENDATIONS
# -------------------------
@app.route('/collaborative_filtering', methods=['GET', 'POST'])
def collaborative_recommend():
    if request.method == 'POST':
        movie_name = request.form.get('movie_name').strip().lower()
        
        # Try exact match first; if not found, fallback to flexible matching
        movie_recommendations = recommendations_df[recommendations_df['name'].str.lower() == movie_name]
        if movie_recommendations.empty:
            movie_recommendations = recommendations_df[recommendations_df['name'].str.lower().str.contains(movie_name)]
        
        if not movie_recommendations.empty:
            # Extract genre from the first matched movie (assuming comma-separated if multiple)
            movie_genre = movie_recommendations.iloc[0]['genre_name']
            
            # Filter movies with matching genre while excluding the original movie
            similar_movies = recommendations_df[
                (recommendations_df['genre_name'].str.contains(movie_genre)) & 
                (recommendations_df['name'].str.lower() != movie_name)
            ]
            # Remove duplicates by movie name
            similar_movies = similar_movies.drop_duplicates(subset=['name'])
            # Sort by predicted rating (descending) and select top 10
            top_10_recommendations = similar_movies[['name', 'genre_name', 'scaled_predicted_rating']].sort_values(
                by='scaled_predicted_rating', ascending=False).head(10)
            return render_template('collaborative.html', movies=top_10_recommendations.to_dict(orient='records'))
        else:
            error = "No recommendations found for this movie name."
            return render_template('collaborative.html', error=error)
    return render_template('collaborative.html')

if __name__ == '__main__':
    app.run(debug=True, port=5500)
