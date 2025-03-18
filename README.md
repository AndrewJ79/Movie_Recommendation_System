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
1. Run ALS model_NB.ipynb:

* Install necessary dependencies (pyspark, pandas, matplotlib, etc.).
* Execute the notebook cells to train the ALS model and generate recommendations.
2. Utilize movie_results.json:

* Load the JSON file into a DataFrame for exploratory analysis.
* Use it to enhance recommendations with metadata filters.
3. Analyze riley.ipynb:

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
