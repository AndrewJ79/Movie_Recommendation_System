# README: Movie Recommendation System
## Overview

This project implements a Movie Recommendation System using both 
Collaborative Filtering and Content-Based Filtering techniques. The 
system provides personalized movie recommendations based on user 
preferences and ratings. The models use the Alternating Least Squares 
(ALS) algorithm for collaborative filtering and metadata for content-based 
filtering.

## Features
* Collaborative Filtering: Uses the Alternating Least Squares 
(ALS) algorithm to predict user-movie ratings.

* Content-Based Filtering: Recommends movies based on their 
content similarity.

* Optimized Model: Hyperparameter tuning is performed to enhance 
the model’s accuracy.

* Interactive Interface: Users can filter recommendations by genre, 
rating, and streaming platform.

## Files and Directories

### Main Code Files

* MRS-collaborative.ipynb: Implements the basic collaborative 
filtering model.

* MRS-collaborative-optimized.ipynb: Implements the optimized 
collaborative filtering model with hyperparameter tuning.

* MRS-content-based.ipynb: Implements the content-based filtering 
model.

* app.py: A Flask application that serves the recommendation models 
via a web interface. The app provides real-time recommendations 
based on both collaborative and content-based filtering approaches, 
and users can filter recommendations by various criteria.

### Resources Folder


* ratings.csv: Contains user ratings for different movies.

* links.csv: Maps MovieLens IDs to TMDB IDs.

* movie_results.json: Contains metadata for movies.

* hyperparameter_tuning.docx: Lists different hyperparameter 
tuning options to test accuracy.

## Running the Model in Google Colab

### Steps to Run:
1. Open Google Colab.
   
2. Upload the necessary resource files (ratings.csv, links.csv, and 
movie_results.json) from the resources folder.

3. Run the Jupyter Notebook:
   * Open and run MRS-collaborative.ipynb for the basic model.

   * Open and run MRS-collaborative-optimized.ipynb for the 
optimized model.

4. You can experiment with different hyperparameters by referencing 
the hyperparameter_tuning.docx file to adjust the model’s 
configurations and check the accuracy.

### Hyperparameter Tuning

The hyperparameter_tuning.docx file includes various options you can 
test to improve the model's performance. Adjusting these parameters will 
allow you to assess the model's accuracy and improve predictions.

### Flask Web Application
* The app.py file runs a Flask web application that provides a user 
interface for movie recommendations. Users can interact with the 
system and receive recommendations based on:
  * Collaborative Filtering (similar movie preferences of users).

  * Content-Based Filtering (based on movie metadata such as 
genre, description, and popularity).

* The app also allows filtering of recommendations by genre, rating, 
and streaming platform.

## How to Use

### Step 1: Set Up the TMDB API Key

1. Create a .env file in the Project4_NB folder.


2. Add the following line to the .env file:
TMDB_API_KEY="API_KEY"

3. Sign up on TMDB and get your own API Key.

4. Copy the API Key and paste it into the .env file where API_KEY is.
   
### Step 2: Open Project in VSCode

1. Open the Movie_Recommendation_System/working_files/NB 
folder in VSCode.

2. Ensure your .env file has a gear icon next to it. If not, just rename it 
within VSCode, and the gear icon should appear.

### Step 3: Run the Flask Application

1. In VSCode, right-click on app.py and open the integrated terminal.

2. In the terminal, run the following command:
python app.py

3. A local server should start, and you will see a message like:
Running on http://127.0.0.1:5500

If the browser doesn’t automatically open, hold Ctrl (or Command on Mac)
and left-click the URL to open the website.
## Notes:

* The MRS-collaborative.ipynb file implements the basic collaborative
filtering model, which serves as a foundation for comparison with the 
optimized model.

* The MRS-collaborative-optimized.ipynb file features the optimized
collaborative filtering model, which has undergone hyperparameter 
tuning for better performance.

* The app.py file serves as the front-end interface, offering real-time 
movie recommendations through both filtering methods.
## Technologies Used
* Python (Pandas, NumPy, Scikit-Learn, Surprise, TensorFlow)
* Jupyter Notebook / Google Colab
* TMDB & MovieLens Datasets
* Flask for web application serving the models
## Contributors
* Val
* Andrew
* Nitu Bola
* Riley

## License
This project is for educational purposes and follows an open-source license. 
Feel free to use, modify, and share the code!
