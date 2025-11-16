🎬 Sentiment Analysis–Based Movie Recommendation System (Backend)
=================================================================

This repository contains the backend implementation for a **Sentiment Analysis–Based Movie Recommendation System**.The system enhances traditional movie recommendations by combining **content-based filtering** with **sentiment analysis** of user reviews, allowing more accurate and personalized results.

⭐ Project Overview
------------------

Traditional recommendation systems rely only on metadata like genres, cast, or plot descriptions.However, this system goes further by:

### 🔍 Using sentiment analysis

*   Analyzes user-generated reviews/comments
    
*   Determines positive/negative sentiment
    
*   Adjusts recommendation scores accordingly
    

### 🎯 Producing refined movie recommendations

*   Content similarity + Review sentiment score
    
*   More accurate than using metadata alone
    
*   Ideal for personalized and trend-aware movie suggestions
    

This backend exposes APIs for recommendation, movie data access, and sentiment-enhanced similarity scoring.

🧩 Key Features
---------------

*   🧠 **Sentiment Analysis Pipeline** (machine learning model or rule-based analyzer)
    
*   🎞 **Hybrid Recommendation Engine**
    
    *   Content-Based Filtering
        
    *   Sentiment-Weighted Scoring
        
*   ⚙️ **Modular Architecture** (datasets, models, routes, services)
    
*   🚀 **Lightweight Python Backend**
    
*   🔌 **Simple REST API Integration** (frontend-ready)
    
*   📂 Organized and extensible codebase
    

📁 Project Structure
--------------------
```
movie_recommendation_system_backend/
│
├── datasets/          # Movie metadata, reviews dataset, sentiment-labeled data
├── models/            # Trained sentiment analysis model, embeddings, similarity files
├── routes/            # REST API route handlers
├── services/          # Sentiment scoring + recommendation logic
├── main.py            # Entry point of backend server
├── requirements.txt   # Dependencies
└── .gitignore
```


🛠 Technologies Used
--------------------

*   **Python**
    
*   **Sentence Transformers** -> all-MiniLM-L6-v2

*   **Sentiment Analysis Model** -> tabularisai/multilingual-sentiment-analysis
    
*   **Scikit-learn**
    
*   **Pandas & NumPy**
    
*   **FastAPI**

*   **Langchain**
  
*  **Hugging Face**  
    

🚀 Getting Started
------------------

### ✔ Prerequisites

*   Python 3.8+
    
*   pip installed
    
*   Virtual environment
    

### 📥 Installation

```bash

git clone https://github.com/souravsaha5703/movie_recommendation_system_backend.git
cd movie_recommendation_system_backend

```

Create a virtual environment:

```bash

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

```

Install required packages:

```bash

pip install -r requirements.txt

```

▶️ Run the Backend
------------------

```bash

uvicorn main:app --reload

```

Backend will start on the configured port.

📡 API Endpoints
----------------

### 🔹 **Get Movie Recommendations**

```bash

GET /api/recommend_movies/movieName

```

Returns top 5 movies similar to the given movie and sentiment analysis.

Returns:

```json

{
    "status": "ok",
    "message": "Movie recommendations fetched successfully",
    "recommendations": [
        {
            "id": "tt6527426",
            "title": "Zero",
            "rating": "5.2",
            "posterUrl": "https://m.media-amazon.com/images/M/MV5BZDQ5ZGFlYjgtMDY4YS00OGQ4LWI4NGItYTczZmIyNDVhNDJlXkEyXkFqcGc@._V1_SX300.jpg"
        },
        {
            "id": "tt8897986",
            "title": "Family of Thakurganj",
            "rating": "5.4",
            "posterUrl": "https://m.media-amazon.com/images/M/MV5BMTk5MzM4ZTMtYWFhMS00NDYyLThkOTQtMWJkOGY1Zjk3ZmYyXkEyXkFqcGdeQXVyODE5NzE3OTE@._V1_SX300.jpg"
        },
        {
            "id": "tt6862542",
            "title": "Hume Tumse Pyaar Kitna",
            "rating": "4.5",
            "posterUrl": "https://m.media-amazon.com/images/M/MV5BNTU3NmYxZmQtODljYy00ZjdiLTk5OTMtYjBmY2UzZmNiMTQ1XkEyXkFqcGc@._V1_SX300.jpg"
        },
        {
            "id": "tt12484724",
            "title": "Mere Desh Ki Dharti",
            "rating": "6.8",
            "posterUrl": "https://m.media-amazon.com/images/M/MV5BNzE0ODI3YjMtOTk5ZC00Nzg4LTgzZDctY2YwMzQ1ZjU3YjQ1XkEyXkFqcGc@._V1_SX300.jpg"
        },
        {
            "id": "tt8033682",
            "title": "Nolok",
            "rating": "7.2",
            "posterUrl": "https://m.media-amazon.com/images/M/MV5BOWM3YzczNDQtYWNjMi00OWI3LWE3MjctYzg5MmM3OTIyNmMwXkEyXkFqcGc@._V1_SX300.jpg"
        }
    ]
}

```

🧠 How the Recommendation System Works
--------------------------------------

![Overall Project Flow](https://res.cloudinary.com/dez9wcn3g/image/upload/v1763302470/movie_recommendaion_system_project_flow_lmacj3.png)


📊 Datasets Used
----------------

Actual Dataset Link :
https://www.kaggle.com/datasets/utsh0dey/25k-movie-dataset

For cleaned and pre-processed dataset open **datasets/** folder.

🤝 Contributing
---------------

Contributions are welcome!

1.  Fork the project
    
2.  Create a new branch
    
3.  Make your feature
    
4.  Push and open a Pull Request
    
💻 Frontend
----------

For frontend part visit https://github.com/souravsaha5703/movie_recommendation_system

📬 Contact
----------

**Author:** Sourav Saha🔗 GitHub: [https://github.com/souravsaha5703](https://github.com/souravsaha5703)

For queries, open an issue in the repository.
