from fastapi import FastAPI
from pydantic import BaseModel

from src.features.build_features import vectorize
from src.models.prediction import predict, recommend
from src.utils.preprocessing import preprocess


class MovieInput(BaseModel):
    title: str
    plot: str


app = FastAPI()


@app.get("/hello")
def hello():
    return {"message": "Hello from AI from Zero to Production workshop"}


@app.post("/classify/")
def classify(request: MovieInput):
    text = request.title + " " + request.plot
    prep_text = preprocess(text)
    x = vectorize(prep_text)
    genre = predict(x)

    return {"title": request.title, "plot": request.plot, "predicted_genre": genre}


@app.post("/similar_movie/")
def similar_movie(request: MovieInput):
    text = request.title + " " + request.plot
    prep_text = preprocess(text)
    x = vectorize(prep_text)
    similar_rows = recommend(x)
    movies = []

    for idx, row in similar_rows.iterrows():
        movies.append(
            {
                "title": row["title"],
                "plot": row["plot"],
                "similarity": row["similarity"],
            }
        )

    return {
        "title": request.title,
        "plot": request.plot,
        "similar_movie": movies,
    }
