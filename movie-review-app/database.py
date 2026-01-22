"""
================================================================================
DATABASE FUNCTIONS FOR THE MOVIE REVIEW APP
================================================================================

This file contains ALL the functions that work with our movie database.
We use SQLite - a simple database that stores data in a single file.

WHAT IS A DATABASE?
-------------------
A database is like a super organized filing cabinet for your data.
Instead of storing data in text files, databases let you:
- Store large amounts of data efficiently
- Search and filter data quickly
- Keep data organized in tables (like spreadsheets)

WHAT IS SQLite?
---------------
SQLite is a lightweight database that:
- Stores everything in ONE file (movies.db)
- Doesn't need a separate server to run
- Is perfect for learning and small applications
- Is used by many real apps (including your phone!)

HOW THIS FILE IS ORGANIZED:
---------------------------
1. Setup functions - Create the database and tables
2. Challenge functions - The coding challenges YOU will complete!

IMPORTANT: Complete the TODO challenges to make the app work!
================================================================================
"""

# ============================================================================
# IMPORTS - These are like toolboxes we need to use
# ============================================================================

# sqlite3 is Python's built-in library for working with SQLite databases
# We use it to run SQL commands and manage our database
import sqlite3


# ============================================================================
# DATABASE CONFIGURATION
# ============================================================================

# This is the name of our database file
# When you run the app, you'll see a file called "movies.db" appear
# All our data (movies and reviews) will be stored inside this file
DATABASE_NAME = "movies.db"


# ============================================================================
# HELPER FUNCTION - GET DATABASE CONNECTION
# ============================================================================

def get_connection():
    """
    Create a connection to our SQLite database.

    WHAT IS A CONNECTION?
    ---------------------
    Think of it like opening a door to the database.
    We need to "connect" before we can read or write any data.

    WHAT IS row_factory?
    --------------------
    By default, SQLite returns data as tuples like: (1, "The Dark Knight", 2008)
    But that's hard to work with! We don't know which value is which.

    Setting row_factory = sqlite3.Row makes it return data like a dictionary:
    {"id": 1, "title": "The Dark Knight", "year": 2008}

    This is MUCH easier to use because we can access values by name!

    Returns:
        sqlite3.Connection: An open connection to the database
    """
    # sqlite3.connect() opens the database file (creates it if it doesn't exist)
    connection = sqlite3.connect(DATABASE_NAME)

    # This makes our results easier to work with (like dictionaries)
    connection.row_factory = sqlite3.Row

    # Return the connection so other functions can use it
    return connection


# ============================================================================
# DATABASE SETUP - CREATE TABLES
# ============================================================================

def create_tables():
    """
    Create the database tables if they don't exist.

    WHAT IS A TABLE?
    ----------------
    A table is like a spreadsheet in your database.
    Each table stores one type of thing (movies or reviews).

    WHAT IS A SCHEMA?
    -----------------
    A schema defines the structure of your table:
    - What columns (fields) it has
    - What type of data each column holds (text, number, etc.)

    OUR TABLES:
    -----------
    1. movies - Stores information about each movie
       Columns: id, title, year, genre, poster, plot

    2. reviews - Stores user reviews for movies
       Columns: id, movie_id, reviewer_name, rating, comment

    WHAT IS A PRIMARY KEY?
    ----------------------
    A primary key is a unique identifier for each row.
    No two rows can have the same primary key.
    We use 'id' as our primary key - each movie/review gets a unique number.

    WHAT IS A FOREIGN KEY?
    ----------------------
    A foreign key links one table to another.
    In the reviews table, movie_id is a foreign key that points to a movie.
    This tells us which movie the review is about.

    WHAT IS AUTOINCREMENT?
    ----------------------
    AUTOINCREMENT means the database automatically assigns the next number.
    So we don't have to manually track what ID to use next!
    """
    # Step 1: Open a connection to the database
    connection = get_connection()

    # Step 2: Get a "cursor" - this is what we use to run SQL commands
    # Think of it like a pen that writes commands to the database
    cursor = connection.cursor()

    # Step 3: Create the movies table
    # The triple quotes (""") let us write multi-line strings
    # IF NOT EXISTS means: only create if the table doesn't already exist
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

    # Step 4: Create the reviews table
    # movie_id links each review to a movie (foreign key relationship)
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

    # Step 5: Save the changes to the database
    # This is called "committing" - without this, changes are lost!
    connection.commit()

    # Step 6: Close the connection (like closing the door)
    # Always close connections when you're done!
    connection.close()


def seed_movies():
    """
    Add initial movie data to the database.

    WHAT IS SEEDING?
    ----------------
    "Seeding" means adding initial/starter data to your database.
    This gives us some movies to display when the app first runs.

    WHY CHECK IF MOVIES EXIST FIRST?
    ---------------------------------
    We don't want to add duplicate movies every time the app starts!
    So we first check if movies already exist in the database.
    If they do, we skip adding them again.

    SQL INSERT STATEMENT:
    ---------------------
    INSERT INTO tablename (column1, column2, ...) VALUES (value1, value2, ...)

    This adds a new row to the table with the specified values.
    """
    # Step 1: Open connection and get cursor
    connection = get_connection()
    cursor = connection.cursor()

    # Step 2: Check if we already have movies in the database
    # SELECT COUNT(*) counts how many rows are in the table
    cursor.execute("SELECT COUNT(*) as count FROM movies")
    result = cursor.fetchone()  # Get the result

    # If we already have movies, don't add duplicates - just return
    if result["count"] > 0:
        connection.close()
        return

    # Step 3: Define our list of movies to add
    # Each movie is a dictionary with all its information
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

    # Step 4: Insert each movie into the database
    # We use a for loop to go through each movie in our list
    for movie in movies:
        # The ? symbols are placeholders for our values
        # This is called a "parameterized query" - it's safe from SQL injection attacks!
        cursor.execute("""
            INSERT INTO movies (title, year, genre, poster, plot)
            VALUES (?, ?, ?, ?, ?)
        """, (movie["title"], movie["year"], movie["genre"], movie["poster"], movie["plot"]))

    # Step 5: Save all the changes
    connection.commit()

    # Step 6: Close the connection
    connection.close()


# ============================================================================
# CHALLENGE 1 - DONE FOR YOU!
# Load all movies from the database
# ============================================================================

def load_movies():
    """
    Load ALL movies from the database.

    CHALLENGE 1 - DONE FOR YOU!
    ---------------------------
    This shows you how to read data from a database using SELECT.

    SQL SELECT STATEMENT:
    ---------------------
    SELECT * FROM tablename

    The * means "all columns" - we want everything!

    HOW IT WORKS:
    -------------
    1. Connect to the database
    2. Run a SELECT query to get all movies
    3. Use fetchall() to get ALL the results as a list
    4. Convert each row to a dictionary (easier to use)
    5. Attach any reviews to each movie
    6. Return the list of movies

    Returns:
        list: A list of all movie dictionaries with their reviews
    """
    # Step 1: Connect to the database
    connection = get_connection()
    cursor = connection.cursor()

    # Step 2: Run SELECT query to get ALL movies
    # SELECT * means "select all columns"
    # FROM movies means "from the movies table"
    cursor.execute("SELECT * FROM movies")

    # Step 3: Fetch all results
    # fetchall() returns a list of all matching rows
    rows = cursor.fetchall()

    # Step 4: Convert each row to a dictionary
    # We also attach any reviews for this movie
    movies = []
    for row in rows:
        # Convert the row to a dictionary
        movie = dict(row)

        # Get reviews for this movie (using the helper function)
        movie["reviews"] = get_reviews_for_movie(movie["id"])

        # Add the movie to our list
        movies.append(movie)

    # Step 5: Close the connection
    connection.close()

    # Step 6: Return the list of movies
    return movies


# ============================================================================
# HELPER FUNCTION - Get reviews for a specific movie
# ============================================================================

def get_reviews_for_movie(movie_id):
    """
    Get all reviews for a specific movie.

    This is a helper function used by other functions.
    It's not a challenge - it's already done for you!

    HOW IT WORKS:
    -------------
    1. Connect to the database
    2. Run SELECT query with WHERE clause to filter by movie_id
    3. Return all matching reviews

    SQL WHERE CLAUSE:
    -----------------
    WHERE column = value

    This filters the results to only include rows where the condition is true.

    Args:
        movie_id (int): The ID of the movie to get reviews for

    Returns:
        list: A list of review dictionaries for this movie
    """
    connection = get_connection()
    cursor = connection.cursor()

    # SELECT reviews WHERE movie_id matches
    # The ? is a placeholder for the movie_id value
    cursor.execute("SELECT * FROM reviews WHERE movie_id = ?", (movie_id,))

    # Convert rows to list of dictionaries
    rows = cursor.fetchall()
    reviews = [dict(row) for row in rows]

    connection.close()
    return reviews


# ============================================================================
# CHALLENGE 2 - YOUR TURN!
# Find a single movie by its ID
# ============================================================================

def get_movie_by_id(movie_id):
    """
    Find a single movie by its ID.

    CHALLENGE 2 - YOUR TURN!
    ========================

    DIFFICULTY: Easy
    TIME: ~10 minutes

    WHAT YOU NEED TO DO:
    --------------------
    Find and return ONE specific movie from the database.

    SQL YOU'LL USE:
    ---------------
    SELECT * FROM movies WHERE id = ?

    This selects ALL columns from movies WHERE the id equals our value.
    The ? is a placeholder - you put the actual value in a tuple.

    STEP-BY-STEP HINTS:
    -------------------
    1. Create a connection: connection = get_connection()
    2. Get a cursor: cursor = connection.cursor()
    3. Run the SELECT query with WHERE clause:
       cursor.execute("SELECT * FROM movies WHERE id = ?", (movie_id,))
       NOTE: The comma after movie_id is important! It makes it a tuple.
    4. Get ONE result: row = cursor.fetchone()
       (fetchone returns ONE row, fetchall returns ALL rows)
    5. Check if movie was found: if row is None: return None
    6. Convert to dictionary: movie = dict(row)
    7. Add reviews: movie["reviews"] = get_reviews_for_movie(movie_id)
    8. Close connection: connection.close()
    9. Return the movie!

    Args:
        movie_id (int): The ID of the movie to find

    Returns:
        dict: The movie dictionary if found, None if not found

    EXAMPLE:
    --------
    movie = get_movie_by_id(1)
    # Returns: {"id": 1, "title": "The Dark Knight", ...}

    movie = get_movie_by_id(999)
    # Returns: None (movie doesn't exist)
    """
    # TODO: Write your code here!
    # Remember to:
    # 1. Connect to database
    # 2. SELECT the movie WHERE id = movie_id
    # 3. Check if found (fetchone might return None)
    # 4. Convert to dict and add reviews
    # 5. Close connection and return
    pass


# ============================================================================
# CHALLENGE 3 - YOUR TURN!
# Save a new review to the database
# ============================================================================

def add_review(movie_id, review):
    """
    Save a new review for a movie to the database.

    CHALLENGE 3 - YOUR TURN!
    ========================

    DIFFICULTY: Medium
    TIME: ~15 minutes

    WHAT YOU NEED TO DO:
    --------------------
    Insert a new review into the reviews table.

    SQL YOU'LL USE:
    ---------------
    INSERT INTO reviews (movie_id, reviewer_name, rating, comment)
    VALUES (?, ?, ?, ?)

    INSERT INTO adds a new row to the table.
    The VALUES are the data for each column.

    THE REVIEW PARAMETER:
    ---------------------
    The 'review' parameter is a dictionary that looks like this:
    {
        "name": "John",
        "rating": 5,
        "comment": "Great movie!"
    }

    You need to extract these values and insert them!

    STEP-BY-STEP HINTS:
    -------------------
    1. Create a connection: connection = get_connection()
    2. Get a cursor: cursor = connection.cursor()
    3. Run the INSERT query:
       cursor.execute('''
           INSERT INTO reviews (movie_id, reviewer_name, rating, comment)
           VALUES (?, ?, ?, ?)
       ''', (movie_id, review["name"], review["rating"], review["comment"]))
    4. IMPORTANT! Commit the changes: connection.commit()
       Without this, the review won't be saved!
    5. Close connection: connection.close()

    Args:
        movie_id (int): The ID of the movie being reviewed
        review (dict): A dictionary with keys: "name", "rating", "comment"

    Returns:
        None (this function doesn't need to return anything)

    EXAMPLE:
    --------
    review = {"name": "Alice", "rating": 5, "comment": "Amazing!"}
    add_review(1, review)
    # This adds a new review for movie with id=1
    """
    # TODO: Write your code here!
    # Remember to:
    # 1. Connect to database
    # 2. INSERT the review into the reviews table
    # 3. COMMIT the changes (very important!)
    # 4. Close connection
    pass


# ============================================================================
# CHALLENGE 4 - YOUR TURN!
# Calculate the average rating for a movie
# ============================================================================

def get_average_rating(movie_id):
    """
    Calculate the average star rating for a movie.

    CHALLENGE 4 - YOUR TURN!
    ========================

    DIFFICULTY: Medium
    TIME: ~15 minutes

    WHAT YOU NEED TO DO:
    --------------------
    Calculate the average (mean) of all ratings for a movie.

    TWO WAYS TO DO THIS:
    --------------------

    METHOD 1 - Using Python (Recommended for beginners):
    1. Get all reviews for the movie
    2. If no reviews, return 0
    3. Add up all the ratings
    4. Divide by the number of reviews
    5. Round to 1 decimal place

    METHOD 2 - Using SQL AVG function (Advanced):
    SELECT AVG(rating) FROM reviews WHERE movie_id = ?
    This calculates the average directly in the database!

    STEP-BY-STEP HINTS (Method 1 - Python):
    ---------------------------------------
    1. Get reviews: reviews = get_reviews_for_movie(movie_id)
    2. Check if empty: if len(reviews) == 0: return 0
    3. Add up ratings with a loop:
       total = 0
       for review in reviews:
           total = total + review["rating"]
    4. Calculate average: average = total / len(reviews)
    5. Round it: return round(average, 1)

    Args:
        movie_id (int): The ID of the movie

    Returns:
        float: The average rating (0 if no reviews)

    EXAMPLE:
    --------
    # If movie 1 has reviews with ratings: 5, 4, 5
    get_average_rating(1)
    # Returns: 4.7 (which is (5+4+5)/3 = 14/3 = 4.666... rounded to 4.7)

    # If movie 2 has no reviews
    get_average_rating(2)
    # Returns: 0
    """
    # TODO: Write your code here!
    # Remember:
    # 1. Get reviews for this movie
    # 2. Handle the case where there are no reviews (return 0)
    # 3. Calculate the average
    # 4. Round to 1 decimal place using round(value, 1)
    return 0


# ============================================================================
# CHALLENGE 5 - YOUR TURN!
# Search for movies by title
# ============================================================================

def search_movies(query):
    """
    Search for movies by title.

    CHALLENGE 5 - YOUR TURN!
    ========================

    DIFFICULTY: Easy
    TIME: ~10 minutes

    WHAT YOU NEED TO DO:
    --------------------
    Search for movies where the title contains the search query.
    The search should be case-insensitive (ignore capitals).

    TWO WAYS TO DO THIS:
    --------------------

    METHOD 1 - Using Python (Recommended for beginners):
    1. If query is empty, return all movies
    2. Load all movies
    3. Filter movies where query is in the title

    METHOD 2 - Using SQL LIKE (Advanced):
    SELECT * FROM movies WHERE LOWER(title) LIKE LOWER('%query%')
    The % symbols mean "anything before/after"

    STEP-BY-STEP HINTS (Method 1 - Python):
    ---------------------------------------
    1. Check if empty query: if query == "": return load_movies()
    2. Load all movies: movies = load_movies()
    3. Convert query to lowercase: query_lower = query.lower()
    4. Create results list: results = []
    5. Loop through movies:
       for movie in movies:
           if query_lower in movie["title"].lower():
               results.append(movie)
    6. Return results

    Args:
        query (str): The search term to look for in movie titles

    Returns:
        list: Movies that match the search (or all movies if query is empty)

    EXAMPLE:
    --------
    search_movies("dark")
    # Returns: [{"title": "The Dark Knight", ...}]

    search_movies("SPIDER")  # Case insensitive!
    # Returns: [{"title": "Spider-Man: Into the Spider-Verse", ...}]

    search_movies("")
    # Returns: all movies
    """
    # TODO: Write your code here!
    # Remember:
    # 1. Handle empty query (return all movies)
    # 2. Make search case-insensitive using .lower()
    # 3. Check if query is IN the title
    # 4. Return matching movies
    return load_movies()


# ============================================================================
# CHALLENGE 6 - YOUR TURN!
# Get the top rated movies
# ============================================================================

def get_top_rated_movies(limit=5):
    """
    Get the top rated movies based on average review ratings.

    CHALLENGE 6 - YOUR TURN!
    ========================

    DIFFICULTY: Medium
    TIME: ~15 minutes

    WHAT YOU NEED TO DO:
    --------------------
    Find movies that have reviews, sort them by rating (highest first),
    and return the top 'limit' movies.

    STEP-BY-STEP HINTS:
    -------------------
    1. Get all movies: movies = load_movies()
    2. Create empty list for rated movies: rated_movies = []
    3. Loop through movies:
       for movie in movies:
           rating = get_average_rating(movie["id"])
           if rating > 0:  # Only include movies WITH reviews
               movie["avg_rating"] = rating
               rated_movies.append(movie)
    4. Sort by rating (highest first):
       sorted_movies = sorted(rated_movies, key=lambda m: m["avg_rating"], reverse=True)

       WHAT IS LAMBDA?
       ---------------
       lambda is a mini function! "lambda m: m["avg_rating"]" means:
       "for each movie m, use its avg_rating value for sorting"

       reverse=True means highest to lowest (descending order)

    5. Return only the first 'limit' movies:
       return sorted_movies[:limit]

       The [:limit] is called "slicing" - it takes the first 'limit' items

    Args:
        limit (int): How many movies to return (default 5)

    Returns:
        list: The top rated movies, sorted from highest to lowest rating

    EXAMPLE:
    --------
    get_top_rated_movies(3)
    # Returns the 3 highest rated movies (only those with reviews)
    """
    # TODO: Write your code here!
    # Remember:
    # 1. Get all movies
    # 2. Calculate average rating for each
    # 3. Only include movies with reviews (rating > 0)
    # 4. Sort by rating (highest first)
    # 5. Return only the first 'limit' movies
    return []


# ============================================================================
# CHALLENGE 7 - YOUR TURN! (BONUS)
# Get movies by genre
# ============================================================================

def get_movies_by_genre(genre):
    """
    Get all movies that match a specific genre.

    CHALLENGE 7 - BONUS CHALLENGE!
    ==============================

    DIFFICULTY: Easy
    TIME: ~10 minutes

    WHAT YOU NEED TO DO:
    --------------------
    Filter movies to only show those matching the given genre.
    The search should be case-insensitive.

    STEP-BY-STEP HINTS:
    -------------------
    1. Load all movies: movies = load_movies()
    2. If genre is empty, return all movies
    3. Convert genre to lowercase: genre_lower = genre.lower()
    4. Filter movies where genre matches:
       results = []
       for movie in movies:
           if movie["genre"].lower() == genre_lower:
               results.append(movie)
    5. Return results

    Args:
        genre (str): The genre to filter by (e.g., "Action", "Drama")

    Returns:
        list: Movies that match the genre

    EXAMPLE:
    --------
    get_movies_by_genre("Action")
    # Returns: [{"title": "The Dark Knight", ...}, {"title": "Avengers: Endgame", ...}]

    get_movies_by_genre("animation")  # Case insensitive!
    # Returns: [{"title": "Spider-Man: Into the Spider-Verse", ...}, ...]
    """
    # TODO: Write your code here!
    # This is a BONUS challenge - try it if you finish the others!
    return load_movies()


# ============================================================================
# CHALLENGE 8 - YOUR TURN! (BONUS)
# Count total reviews for a movie
# ============================================================================

def count_reviews(movie_id):
    """
    Count how many reviews a movie has.

    CHALLENGE 8 - BONUS CHALLENGE!
    ==============================

    DIFFICULTY: Easy
    TIME: ~5 minutes

    WHAT YOU NEED TO DO:
    --------------------
    Return the number of reviews for a specific movie.

    TWO WAYS TO DO THIS:
    --------------------

    METHOD 1 - Using Python:
    reviews = get_reviews_for_movie(movie_id)
    return len(reviews)

    METHOD 2 - Using SQL COUNT:
    SELECT COUNT(*) FROM reviews WHERE movie_id = ?

    Args:
        movie_id (int): The ID of the movie

    Returns:
        int: The number of reviews for this movie

    EXAMPLE:
    --------
    count_reviews(1)
    # Returns: 3 (if movie 1 has 3 reviews)

    count_reviews(999)
    # Returns: 0 (movie has no reviews)
    """
    # TODO: Write your code here!
    # This is a BONUS challenge - try it if you finish the others!
    return 0


# ============================================================================
# CHALLENGE 9 - YOUR TURN! (BONUS - ADVANCED)
# Get all unique genres
# ============================================================================

def get_all_genres():
    """
    Get a list of all unique genres in the database.

    CHALLENGE 9 - BONUS CHALLENGE (ADVANCED)!
    =========================================

    DIFFICULTY: Medium
    TIME: ~10 minutes

    WHAT YOU NEED TO DO:
    --------------------
    Return a list of all different genres (no duplicates).

    METHOD 1 - Using Python:
    1. Load all movies
    2. Create an empty list for genres
    3. Loop through movies and collect unique genres
    4. Sort alphabetically (optional but nice)

    METHOD 2 - Using SQL DISTINCT:
    SELECT DISTINCT genre FROM movies
    DISTINCT means "only unique values"

    Args:
        None

    Returns:
        list: A list of unique genre strings

    EXAMPLE:
    --------
    get_all_genres()
    # Returns: ["Action", "Animation", "Crime", "Drama", "Sci-Fi"]
    """
    # TODO: Write your code here!
    # This is a BONUS challenge - try it if you finish the others!
    return []


# ============================================================================
# CHALLENGE 10 - YOUR TURN! (BONUS - ADVANCED)
# Delete a review
# ============================================================================

def delete_review(review_id):
    """
    Delete a review from the database.

    CHALLENGE 10 - BONUS CHALLENGE (ADVANCED)!
    ==========================================

    DIFFICULTY: Medium
    TIME: ~10 minutes

    WHAT YOU NEED TO DO:
    --------------------
    Remove a review from the database using its ID.

    SQL YOU'LL USE:
    ---------------
    DELETE FROM reviews WHERE id = ?

    DELETE removes rows from the table.
    WHERE specifies which row(s) to delete.

    STEP-BY-STEP HINTS:
    -------------------
    1. Create connection
    2. Get cursor
    3. Run DELETE query: cursor.execute("DELETE FROM reviews WHERE id = ?", (review_id,))
    4. Commit changes!
    5. Close connection

    Args:
        review_id (int): The ID of the review to delete

    Returns:
        None

    EXAMPLE:
    --------
    delete_review(1)
    # Removes the review with id=1 from the database
    """
    # TODO: Write your code here!
    # This is a BONUS challenge - try it if you finish the others!
    pass


# ============================================================================
# INITIALIZATION - Run when the app starts
# ============================================================================

# This code runs automatically when this file is loaded
# It makes sure our database and tables exist before the app starts

# Create the tables (if they don't exist)
create_tables()

# Add initial movie data (if not already added)
seed_movies()
