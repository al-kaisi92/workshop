"""
================================================================================
DATABASE FUNCTIONS FOR THE MOVIE REVIEW APP - SOLUTION FILE
================================================================================

THIS IS THE COMPLETE SOLUTION FILE!
Students should work in the movie-review-app folder, not this one!

This file shows the completed versions of all challenges.
Use this as a reference if students get stuck.

================================================================================
"""

# ============================================================================
# IMPORTS
# ============================================================================

# sqlite3 is Python's built-in library for working with SQLite databases
import sqlite3


# ============================================================================
# DATABASE CONFIGURATION
# ============================================================================

# This is the name of our database file
DATABASE_NAME = "movies.db"


# ============================================================================
# HELPER FUNCTION - GET DATABASE CONNECTION
# ============================================================================

def get_connection():
    """
    Create a connection to our SQLite database.
    Returns:
        sqlite3.Connection: An open connection to the database
    """
    # Open the database file (creates it if it doesn't exist)
    connection = sqlite3.connect(DATABASE_NAME)

    # Makes results easier to work with (like dictionaries)
    connection.row_factory = sqlite3.Row

    return connection


# ============================================================================
# DATABASE SETUP - CREATE TABLES
# ============================================================================

def create_tables():
    """
    Create the database tables if they don't exist.
    """
    connection = get_connection()
    cursor = connection.cursor()

    # Create movies table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            year INTEGER NOT NULL,
            genre TEXT NOT NULL,
            poster TEXT NOT NULL,
            plot TEXT NOT NULL
        )
    """)

    # Create reviews table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            movie_id INTEGER NOT NULL,
            reviewer_name TEXT NOT NULL,
            rating INTEGER NOT NULL,
            comment TEXT NOT NULL,
            FOREIGN KEY (movie_id) REFERENCES movies (id)
        )
    """)

    connection.commit()
    connection.close()


def seed_movies():
    """
    Add initial movie data to the database.
    """
    connection = get_connection()
    cursor = connection.cursor()

    # Check if we already have movies
    cursor.execute("SELECT COUNT(*) as count FROM movies")
    result = cursor.fetchone()

    if result["count"] > 0:
        connection.close()
        return

    # Our list of movies
    movies = [
        {
            "title": "The Dark Knight",
            "year": 2008,
            "genre": "Action",
            "poster": "https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SX300.jpg",
            "plot": "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice."
        },
        {
            "title": "Inception",
            "year": 2010,
            "genre": "Sci-Fi",
            "poster": "https://m.media-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SX300.jpg",
            "plot": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O."
        },
        {
            "title": "Spider-Man: Into the Spider-Verse",
            "year": 2018,
            "genre": "Animation",
            "poster": "https://m.media-amazon.com/images/M/MV5BMjMwNDkxMTgzOF5BMl5BanBnXkFtZTgwNTkwNTQ3NjM@._V1_SX300.jpg",
            "plot": "Teen Miles Morales becomes the Spider-Man of his universe, and must join with five spider-powered individuals from other dimensions to stop a threat for all realities."
        },
        {
            "title": "The Shawshank Redemption",
            "year": 1994,
            "genre": "Drama",
            "poster": "https://m.media-amazon.com/images/M/MV5BNDE3ODcxYzMtY2YzZC00NmNlLWJiNDMtZDViZWM2MzIxZDYwXkEyXkFqcGdeQXVyNjAwNDUxODI@._V1_SX300.jpg",
            "plot": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency."
        },
        {
            "title": "Interstellar",
            "year": 2014,
            "genre": "Sci-Fi",
            "poster": "https://m.media-amazon.com/images/M/MV5BZjdkOTU3MDktN2IxOS00OGEyLWFmMjktY2FiMmZkNWIyODZiXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SX300.jpg",
            "plot": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival."
        },
        {
            "title": "The Lion King",
            "year": 1994,
            "genre": "Animation",
            "poster": "https://m.media-amazon.com/images/M/MV5BYTYxNGMyZTYtMjE3MS00MzNjLWFjNmYtMDk3N2FmM2JiM2M1XkEyXkFqcGdeQXVyNjY5NDU4NzI@._V1_SX300.jpg",
            "plot": "Lion prince Simba and his father are targeted by his bitter uncle, who wants to ascend the throne himself."
        },
        {
            "title": "Avengers: Endgame",
            "year": 2019,
            "genre": "Action",
            "poster": "https://m.media-amazon.com/images/M/MV5BMTc5MDE2ODcwNV5BMl5BanBnXkFtZTgwMzI2NzQ2NzM@._V1_SX300.jpg",
            "plot": "After the devastating events of Infinity War, the Avengers assemble once more to reverse Thanos' actions and restore balance to the universe."
        },
        {
            "title": "Parasite",
            "year": 2019,
            "genre": "Drama",
            "poster": "https://m.media-amazon.com/images/M/MV5BYWZjMjk3ZTItODQ2ZC00NTY5LWE0ZDYtZTI3MjcwN2Q5NTVkXkEyXkFqcGdeQXVyODk4OTc3MTY@._V1_SX300.jpg",
            "plot": "Greed and class discrimination threaten the newly formed symbiotic relationship between the wealthy Park family and the destitute Kim clan."
        },
        {
            "title": "The Matrix",
            "year": 1999,
            "genre": "Sci-Fi",
            "poster": "https://m.media-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SX300.jpg",
            "plot": "A computer hacker learns about the true nature of reality and his role in the war against its controllers."
        },
        {
            "title": "Forrest Gump",
            "year": 1994,
            "genre": "Drama",
            "poster": "https://m.media-amazon.com/images/M/MV5BNWIwODRlZTUtY2U3ZS00Yzg1LWJhNzYtMmZiYmEyNmU1NjMzXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg",
            "plot": "The history of the United States from the 1950s to the '70s unfolds from the perspective of an Alabama man with an IQ of 75."
        },
        {
            "title": "Toy Story",
            "year": 1995,
            "genre": "Animation",
            "poster": "https://m.media-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_SX300.jpg",
            "plot": "A cowboy doll is profoundly threatened and jealous when a new spaceman action figure supplants him as top toy in a boy's bedroom."
        },
        {
            "title": "Pulp Fiction",
            "year": 1994,
            "genre": "Crime",
            "poster": "https://m.media-amazon.com/images/M/MV5BNGNhMDIzZTUtNTBlZi00MTRlLWFjM2ItYzViMjE3YzI5MjljXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SX300.jpg",
            "plot": "The lives of two mob hitmen, a boxer, a gangster and his wife intertwine in four tales of violence and redemption."
        }
    ]

    # Insert each movie
    for movie in movies:
        cursor.execute("""
            INSERT INTO movies (title, year, genre, poster, plot)
            VALUES (?, ?, ?, ?, ?)
        """, (movie["title"], movie["year"], movie["genre"], movie["poster"], movie["plot"]))

    connection.commit()
    connection.close()


# ============================================================================
# CHALLENGE 1 - DONE FOR STUDENTS
# ============================================================================

def load_movies():
    """Load ALL movies from the database."""
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM movies")
    rows = cursor.fetchall()

    movies = []
    for row in rows:
        movie = dict(row)
        movie["reviews"] = get_reviews_for_movie(movie["id"])
        movies.append(movie)

    connection.close()
    return movies


def get_reviews_for_movie(movie_id):
    """Get all reviews for a specific movie."""
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM reviews WHERE movie_id = ?", (movie_id,))
    rows = cursor.fetchall()
    reviews = [dict(row) for row in rows]

    connection.close()
    return reviews


# ============================================================================
# CHALLENGE 2 - SOLUTION
# ============================================================================

def get_movie_by_id(movie_id):
    """
    Find a single movie by its ID.

    CHALLENGE 2 - SOLUTION
    """
    # Step 1: Connect to database
    connection = get_connection()
    cursor = connection.cursor()

    # Step 2: SELECT the movie WHERE id matches
    cursor.execute("SELECT * FROM movies WHERE id = ?", (movie_id,))

    # Step 3: Get ONE result
    row = cursor.fetchone()

    # Step 4: Check if movie was found
    if row is None:
        connection.close()
        return None

    # Step 5: Convert to dictionary
    movie = dict(row)

    # Step 6: Add reviews
    movie["reviews"] = get_reviews_for_movie(movie_id)

    # Step 7: Close connection
    connection.close()

    # Step 8: Return the movie
    return movie


# ============================================================================
# CHALLENGE 3 - SOLUTION
# ============================================================================

def add_review(movie_id, review):
    """
    Save a new review for a movie.

    CHALLENGE 3 - SOLUTION
    """
    # Step 1: Connect to database
    connection = get_connection()
    cursor = connection.cursor()

    # Step 2: INSERT the review
    cursor.execute("""
        INSERT INTO reviews (movie_id, reviewer_name, rating, comment)
        VALUES (?, ?, ?, ?)
    """, (movie_id, review["name"], review["rating"], review["comment"]))

    # Step 3: COMMIT the changes (very important!)
    connection.commit()

    # Step 4: Close connection
    connection.close()


# ============================================================================
# CHALLENGE 4 - SOLUTION
# ============================================================================

def get_average_rating(movie_id):
    """
    Calculate the average star rating for a movie.

    CHALLENGE 4 - SOLUTION
    """
    # Step 1: Get reviews for this movie
    reviews = get_reviews_for_movie(movie_id)

    # Step 2: If no reviews, return 0
    if len(reviews) == 0:
        return 0

    # Step 3: Add up all ratings
    total = 0
    for review in reviews:
        total = total + review["rating"]

    # Step 4: Calculate average
    average = total / len(reviews)

    # Step 5: Round to 1 decimal place and return
    return round(average, 1)


# ============================================================================
# CHALLENGE 5 - SOLUTION
# ============================================================================

def search_movies(query):
    """
    Search for movies by title.

    CHALLENGE 5 - SOLUTION
    """
    # Step 1: If query is empty, return all movies
    if query == "":
        return load_movies()

    # Step 2: Load all movies
    movies = load_movies()

    # Step 3: Convert query to lowercase for case-insensitive search
    query_lower = query.lower()

    # Step 4: Create results list
    results = []

    # Step 5: Loop through movies and find matches
    for movie in movies:
        if query_lower in movie["title"].lower():
            results.append(movie)

    # Step 6: Return results
    return results


# ============================================================================
# CHALLENGE 6 - SOLUTION
# ============================================================================

def get_top_rated_movies(limit=5):
    """
    Get the top rated movies based on average review ratings.

    CHALLENGE 6 - SOLUTION
    """
    # Step 1: Get all movies
    movies = load_movies()

    # Step 2: Create empty list for rated movies
    rated_movies = []

    # Step 3: Loop through movies
    for movie in movies:
        rating = get_average_rating(movie["id"])

        # Only include movies WITH reviews
        if rating > 0:
            movie["avg_rating"] = rating
            rated_movies.append(movie)

    # Step 4: Sort by rating (highest first)
    sorted_movies = sorted(rated_movies, key=lambda m: m["avg_rating"], reverse=True)

    # Step 5: Return only the first 'limit' movies
    return sorted_movies[:limit]


# ============================================================================
# CHALLENGE 7 - SOLUTION (BONUS)
# ============================================================================

def get_movies_by_genre(genre):
    """
    Get all movies that match a specific genre.

    CHALLENGE 7 - BONUS SOLUTION
    """
    # Step 1: Load all movies
    movies = load_movies()

    # Step 2: If genre is empty, return all movies
    if genre == "":
        return movies

    # Step 3: Convert genre to lowercase
    genre_lower = genre.lower()

    # Step 4: Filter movies
    results = []
    for movie in movies:
        if movie["genre"].lower() == genre_lower:
            results.append(movie)

    # Step 5: Return results
    return results


# ============================================================================
# CHALLENGE 8 - SOLUTION (BONUS)
# ============================================================================

def count_reviews(movie_id):
    """
    Count how many reviews a movie has.

    CHALLENGE 8 - BONUS SOLUTION
    """
    # Get reviews and return the count
    reviews = get_reviews_for_movie(movie_id)
    return len(reviews)


# ============================================================================
# CHALLENGE 9 - SOLUTION (BONUS)
# ============================================================================

def get_all_genres():
    """
    Get a list of all unique genres in the database.

    CHALLENGE 9 - BONUS SOLUTION
    """
    # Method 1: Using Python
    movies = load_movies()
    genres = []

    for movie in movies:
        if movie["genre"] not in genres:
            genres.append(movie["genre"])

    # Sort alphabetically
    genres.sort()
    return genres


# ============================================================================
# CHALLENGE 10 - SOLUTION (BONUS)
# ============================================================================

def delete_review(review_id):
    """
    Delete a review from the database.

    CHALLENGE 10 - BONUS SOLUTION
    """
    # Step 1: Connect to database
    connection = get_connection()
    cursor = connection.cursor()

    # Step 2: DELETE the review
    cursor.execute("DELETE FROM reviews WHERE id = ?", (review_id,))

    # Step 3: Commit changes
    connection.commit()

    # Step 4: Close connection
    connection.close()


# ============================================================================
# INITIALIZATION
# ============================================================================

create_tables()
seed_movies()
