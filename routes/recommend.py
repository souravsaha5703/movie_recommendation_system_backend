from fastapi import APIRouter,HTTPException
from services.get_movie_details import get_movie_details_from_omdb,get_reviews,all_movie_details
from services.generate_query import generate_query
from services.recommend_movies import recommend,recommend_based_on_sentiment

router = APIRouter()

@router.get('/health_check',tags=['Health Check'])
def health_check():
    return {"status": "ok", "message": "Movie Recommendation Backend is healthy!"}

@router.get('/recommend_movies/{movieName}')
def recommend_movies(movieName:str):
    try:
        movie_details = get_movie_details_from_omdb(movieName)
        query = generate_query(movie_details)
        recommendation = recommend(query)
        reviews = get_reviews(recommendation['ids'])
        final_recommendation = recommend_based_on_sentiment(reviews,recommendation['movies'])
        final_list = all_movie_details(final_recommendation)
        return {"status": "ok","message":"Movie recommendations fetched successfully" ,"recommendations":final_list}
    
    except Exception as e:
        raise HTTPException(
            status_code=503, 
            detail=f"Something went wrong. Details: {str(e)}"
        )