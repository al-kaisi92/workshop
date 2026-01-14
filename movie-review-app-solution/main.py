from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from database import load_movies, get_movie_by_id, add_review, get_average_rating, search_movies

app = FastAPI()

# Mount static files (CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up templates
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    """Home page - displays all movies"""
    movies = load_movies()

    # Add average rating to each movie for display
    for movie in movies:
        movie["avg_rating"] = get_average_rating(movie["id"])

    return templates.TemplateResponse("index.html", {
        "request": request,
        "movies": movies
    })


@app.get("/movie/{movie_id}", response_class=HTMLResponse)
def movie_detail(request: Request, movie_id: int):
    """Movie detail page - shows one movie with its reviews"""
    movie = get_movie_by_id(movie_id)

    if movie is None:
        return templates.TemplateResponse("error.html", {
            "request": request,
            "message": "Movie not found"
        })

    avg_rating = get_average_rating(movie_id)

    return templates.TemplateResponse("movie.html", {
        "request": request,
        "movie": movie,
        "avg_rating": avg_rating
    })


@app.post("/movie/{movie_id}/review")
def submit_review(
    movie_id: int,
    reviewer_name: str = Form(...),
    rating: int = Form(...),
    comment: str = Form(...)
):
    """Handle review form submission"""
    review = {
        "name": reviewer_name,
        "rating": rating,
        "comment": comment
    }

    add_review(movie_id, review)

    # Redirect back to the movie page
    return RedirectResponse(url=f"/movie/{movie_id}", status_code=303)


@app.get("/search", response_class=HTMLResponse)
def search(request: Request, q: str = ""):
    """Search for movies by title"""
    movies = search_movies(q)

    # Add average rating to each movie
    for movie in movies:
        movie["avg_rating"] = get_average_rating(movie["id"])

    return templates.TemplateResponse("index.html", {
        "request": request,
        "movies": movies,
        "search_query": q
    })


# Run with: uvicorn main:app --reload
