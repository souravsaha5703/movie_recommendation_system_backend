import requests
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

OMDB_API_KEY = os.environ.get('OMDB_KEY')

OMDB_URL = 'http://www.omdbapi.com/'

RAPID_API_KEY =os.environ.get('RAPID_API_KEY')

RAPID_API_SCRAPER_URL = 'https://imdb-scraper4.p.rapidapi.com/'

def get_movie_details_from_omdb(movie:str):
    parameters = {
        'apikey': OMDB_API_KEY,
        't':movie
    }

    try:
        response = requests.get(OMDB_URL, params=parameters)
        response.raise_for_status()

        data = response.json()
        return data

    except requests.exceptions.RequestException as e:
        raise Exception(f"Network/Connection Error: Could not connect to the omdb API. Details: {e}")

    except requests.exceptions.HTTPError as e:
        raise Exception(f"OMDB API Status Error: Received status code {e.response.status_code}")

    except Exception as e:
        raise Exception(f"An unknown error occurred during detail fetch: {str(e)}")    

def get_reviews(recommendation):
    all_movie_reviews = {}

    for id in recommendation:
        querystring = {"work_type":"reviews_imdb","keyword_1":id,"keyword_2":"5"}

        headers = {
	        "x-rapidapi-key": RAPID_API_KEY,
	        "x-rapidapi-host": "imdb-scraper4.p.rapidapi.com"
        }

        try:
            response = requests.get(RAPID_API_SCRAPER_URL, headers=headers, params=querystring)
            response.raise_for_status()

            data = response.json()

            reviews = []

            for r in data:
              reviews.append(r['text'])

            all_movie_reviews[id] = reviews

        except requests.exceptions.RequestException as e:
            raise Exception(f"Network/Connection Error: Could not connect to the API. Details: {e}")

        except requests.exceptions.HTTPError as e:
            raise Exception(f"Rapid API Status Error: Received status code {e.response.status_code}")

        except Exception as e:
            raise Exception(f"An unknown error occurred during detail fetch: {str(e)}")
    
    return all_movie_reviews

def all_movie_details(final_recommendation):
    df = pd.DataFrame(final_recommendation)
    recommendation_list = df.to_dict(orient='records')

    final_detailed_list = []

    for movie in recommendation_list:
        parameters = {
            'apikey': OMDB_API_KEY,
            'i':movie.get('imdb_id')
        }

        try:
            response = requests.get(OMDB_URL, params=parameters)
            response.raise_for_status()

            data = response.json()
            final_detailed_list.append({
                'id':data['imdbID'],
                'title':data['Title'],
                'rating':data['imdbRating'],
                'posterUrl':data['Poster']
            })

        except requests.exceptions.RequestException as e:
            raise Exception(f"Network/Connection Error: Could not connect to the omdb API. Details: {e}")

        except requests.exceptions.HTTPError as e:
            raise Exception(f"OMDB API Status Error: Received status code {e.response.status_code}")

        except Exception as e:
            raise Exception(f"An unknown error occurred during detail fetch: {str(e)}")
    
    return final_detailed_list