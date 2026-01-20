"""
Database functions for the Movie Review App - SOLUTION FILE

This is the completed solution. Students should work in the
movie-review-app folder, not this one!
"""

import json

# This stores reviews in memory (resets when server restarts)
reviews_storage = {}


def load_movies():
    """
    Load all movies from the JSON file.

    CHALLENGE 1 - DONE FOR YOU!
    This shows you how to read data from a JSON file.

    Returns:
        list: A list of movie dictionaries
    """
    with open("data/movies.json", "r") as file:
        movies = json.load(file)

    # Attach any saved reviews to each movie
    for movie in movies:
        movie["reviews"] = reviews_storage.get(movie["id"], [])

    return movies


def get_movie_by_id(movie_id):
    """
    Find a single movie by its ID.

    CHALLENGE 2 - SOLUTION
    """
    movies = load_movies()
    for movie in movies:
        if movie["id"] == movie_id:
            return movie
    return None


def add_review(movie_id, review):
    """
    Save a new review for a movie.

    CHALLENGE 3 - SOLUTION
    """
    if movie_id not in reviews_storage:
        reviews_storage[movie_id] = []
    reviews_storage[movie_id].append(review)


def get_average_rating(movie_id):
    """
    Calculate the average star rating for a movie.

    CHALLENGE 4 - SOLUTION
    """
    movie = get_movie_by_id(movie_id)
    if movie is None:
        return 0

    reviews = movie.get("reviews", [])
    if len(reviews) == 0:
        return 0

    total = 0
    for review in reviews:
        total = total + review["rating"]

    average = total / len(reviews)
    return round(average, 1)


def search_movies(query):
    """
    Search for movies by title.

    CHALLENGE 5 - SOLUTION
    """
    movies = load_movies()

    if query == "":
        return movies

    query_lower = query.lower()
    results = []

    for movie in movies:
        if query_lower in movie["title"].lower():
            results.append(movie)

    return results


def get_top_rated_movies(limit=5):
    """
    Get the top rated movies based on average review ratings.

    CHALLENGE 6 - SOLUTION
    """
    movies = load_movies()
    rated_movies = []

    for movie in movies:
        rating = get_average_rating(movie["id"])
        if rating > 0:
            movie["avg_rating"] = rating
            rated_movies.append(movie)

    sorted_movies = sorted(rated_movies, key=lambda m: m["avg_rating"], reverse=True)
    return sorted_movies[:limit]
