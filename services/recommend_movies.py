import os
from transformers import pipeline
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np

CUSTOM_CACHE_DIR = r"D:\HuggingFace_Cache"

os.environ['HF_HOME'] = CUSTOM_CACHE_DIR

embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

movie_embeddings_path = 'models/movie_embeddings.npy'
movies_dataset_path = 'datasets/movies_dataset.csv'

movie_embeddings = np.load(movie_embeddings_path)
movies = pd.read_csv(movies_dataset_path)

pipe = pipeline("text-classification",model='tabularisai/multilingual-sentiment-analysis')

def recommend(query):
    query_vec = embedding_model.encode([query])
    scores = cosine_similarity(query_vec, movie_embeddings).flatten()
    indices = scores.argsort()[-10:][::-1]
    movie_results = movies.iloc[indices][['movie_title','imdb_id']]
    movie_ids = movie_results['imdb_id'].tolist()
    return {'movies':movie_results,'ids':movie_ids}

def get_positive_score(movie):
    positive_scores = [s['score'] for s in movie['sentiment_scores'] if s['label'] in ['Very Positive','Positive']]

    if not positive_scores:
        return 0
    return sum(positive_scores) / len(positive_scores)

def recommend_based_on_sentiment(reviews,movies):
    all_movie_sentiments = []

    for movie_id,reviews in reviews.items():
        results = pipe(reviews,truncation=True)
        all_movie_sentiments.append({
            'movie_id':movie_id,
            'sentiment_scores':results
        })
    
    for movie in all_movie_sentiments:
        movies['score'] = get_positive_score(movie)
    
    movie_df = pd.DataFrame(movies)
    top_movies = movie_df.sort_values(by='score',ascending=False).head(5)
    return top_movies