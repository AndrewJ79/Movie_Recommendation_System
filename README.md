# README: Movie Recommendation and Analysis Project
## Overview
This project focuses on implementing an ALS (Alternating Least Squares) model for movie recommendations using collaborative filtering. The analysis is supplemented with insights derived from movie metadata and processed datasets.

## Files
1. ALS model_NB.ipynb

* This Jupyter Notebook implements an ALS model for collaborative filtering-based movie recommendations.
* Key steps:
    * Data loading and preprocessing.
    * Matrix factorization using ALS.
    * Model training, hyperparameter tuning, and evaluation.
    * Generating movie recommendations based on user preferences.
2. riley.ipynb

* This notebook might contain additional data processing, analysis, or visualization tasks to support the recommendation system.
* It could include feature engineering, exploratory data analysis (EDA), or alternative modeling approaches.
3. movie_results.json

* A JSON dataset containing metadata for various movies.
* Information includes:
    * Movie title, genres, release date, runtime, and popularity.
    * Production companies and countries.
    * IMDB ratings and vote counts.
    * Taglines and brief overviews.
* This dataset serves as input for the recommendation engine, enabling filtering based on genres, popularity, and user preferences.
4. Files needed to download so you can run the code

* These files just download it to the resources folder
* https://docsend.com/view/s/dd7ffi2pkm4fhuu9
## How to Use
1.Added Api key and .env File

* First Thing you need to do is Added a .env file to Project4_NB Folder and put TMDB_API_KEY="API_KEY" 
* Second sign up on TMDB and get your self a API KEY then copy the and you will and you will paste it in the .evn file where API_KEY is
2. Files needed to download so you can run the code

* These files just download it to the resources folder
* https://docsend.com/view/s/dd7ffi2pkm4fhuu9
3.Open Project4_NB Folder in VSCode

* Make sure your .env File has a Gear Icon next to it if not then just rename it in VSCode and it will work that way
* After that you wil right click on the app.py file and open in integrated terminal and run this code "Python App.py" in the integrated terminal
* A website should pop up but if not there will be an https in the pop up and it will look like this "Running on http://127.0.0.1:5500" and just press Ctrl or command Key and left click 

* If additional analysis is required, review this notebook for supplementary insights or data transformations.
## Dependencies
* Python 3.x
* Jupyter Notebook
* PySpark (for ALS implementation)
* Pandas, NumPy, Matplotlib (for data handling and visualization)
## Future Improvements
* Hybrid Recommendations: Combining ALS with content-based filtering.
* User Interface: Developing a web-based UI for real-time recommendations.
* Enhanced Data: Adding user reviews and sentiment analysis for better personalization.
