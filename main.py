from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.recommend import router

app = FastAPI(title="Sentiment Analysis based Movie Recommendation System")

origins = [
    "http://localhost:5173",
    "http://localhost:3000",
    "http://localhost:5174",
    "https://cinefusionai.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router,prefix="/api")