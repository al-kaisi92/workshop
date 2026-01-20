"""
Database functions for the Movie Review App

This file contains all the functions that work with movie data.
Complete the TODO challenges to make the app work!
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

    CHALLENGE 2 - YOUR TURN!

    Args:
        movie_id (int): The ID of the movie to find

    Returns:
        dict: The movie if found, None if not found

    Hints:
        1. First, call load_movies() to get all movies
        2. Loop through the movies with: for movie in movies:
        3. Check if movie["id"] equals movie_id
        4. If it matches, return that movie
        5. If no match found after the loop, return None
    """
    # TODO: Write your code here!
    pass


def add_review(movie_id, review):
    """
    Save a new review for a movie.

    CHALLENGE 3 - YOUR TURN!

    Args:
        movie_id (int): The ID of the movie being reviewed
        review (dict): The review data containing 'name', 'rating', 'comment'

    Hints:
        1. Check if movie_id exists in reviews_storage
        2. If not, create an empty list: reviews_storage[movie_id] = []
        3. Append the review to the list: reviews_storage[movie_id].append(review)
    """
    # TODO: Write your code here!
    pass


def get_average_rating(movie_id):
    """
    Calculate the average star rating for a movie.

    CHALLENGE 4 - YOUR TURN!

    Args:
        movie_id (int): The ID of the movie

    Returns:
        float: The average rating (0 if no reviews)

    Hints:
        1. Get the movie using get_movie_by_id(movie_id)
        2. If no movie found, return 0
        3. Get the reviews: reviews = movie.get("reviews", [])
        4. If no reviews, return 0
        5. Add up all ratings using a loop
        6. Divide total by number of reviews
        7. Use round(average, 1) to round to 1 decimal place
    """
    # TODO: Write your code here!
    return 0


def search_movies(query):
    """
    Search for movies by title.

    CHALLENGE 5 - YOUR TURN!

    Args:
        query (str): The search term

    Returns:
        list: Movies that match the search

    Hints:
        1. If query is empty, return all movies: load_movies()
        2. Convert query to lowercase: query.lower()
        3. Loop through movies
        4. Check if query is in the movie title (also lowercase)
        5. Add matching movies to a results list
        6. Return the results
    """
    # TODO: Write your code here!
    return load_movies()


def get_top_rated_movies(limit=5):
    """
    Get the top rated movies based on average review ratings.

    CHALLENGE 6 - YOUR TURN!

    Args:
        limit (int): How many movies to return (default 5)

    Returns:
        list: The top rated movies, sorted from highest to lowest

    Hints:
        1. Get all movies using load_movies()
        2. Create an empty list for movies with ratings
        3. Loop through each movie
        4. Get the average rating using get_average_rating(movie["id"])
        5. Only include movies that have reviews (rating > 0)
        6. Add the rating to the movie: movie["avg_rating"] = rating
        7. Append the movie to your list
        8. Sort the list by avg_rating (highest first)
           Hint: Use sorted() with key=lambda m: m["avg_rating"], reverse=True
        9. Return only the first 'limit' movies using [:limit]
    """
    # TODO: Write your code here!
    return []
