"""
================================================================================
DATABASE FUNCTIONS FOR THE MOVIE REVIEW APP - SOLUTION FILE
================================================================================

THIS IS THE COMPLETE SOLUTION FILE!
Students should work in the movie-review-app folder, not this one!

This file shows the completed versions of all challenges using SQLAlchemy.
Use this as a reference if students get stuck.

================================================================================
"""

# ============================================================================
# IMPORTS
# ============================================================================

from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import datetime


# ============================================================================
# DATABASE CONFIGURATION
# ============================================================================

DATABASE_URL = "sqlite:///movies.db"
engine = create_engine(DATABASE_URL, echo=False)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# ============================================================================
# DATABASE MODELS
# ============================================================================

class Movie(Base):
    """Movie model representing the movies table."""
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    year = Column(Integer, nullable=False)
    genre = Column(String(50), nullable=False)
    poster = Column(String(500), nullable=False)
    plot = Column(Text, nullable=False)

    reviews = relationship("Review", back_populates="movie")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "year": self.year,
            "genre": self.genre,
            "poster": self.poster,
            "plot": self.plot,
            "reviews": [review.to_dict() for review in self.reviews]
        }


class Review(Base):
    """Review model representing the reviews table."""
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    movie_id = Column(Integer, ForeignKey("movies.id"), nullable=False)
    reviewer_name = Column(String(100), nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.now)

    movie = relationship("Movie", back_populates="reviews")

    def to_dict(self):
        return {
            "id": self.id,
            "movie_id": self.movie_id,
            "reviewer_name": self.reviewer_name,
            "name": self.reviewer_name,
            "rating": self.rating,
            "comment": self.comment,
            "created_at": self.created_at.strftime("%d %b %Y at %H:%M") if self.created_at else None
        }


# ============================================================================
# DATABASE SETUP
# ============================================================================

def create_tables():
    """Create all database tables."""
    Base.metadata.create_all(bind=engine)


def get_session():
    """Create a new database session."""
    return SessionLocal()


def seed_movies():
    """Add initial movie data to the database."""
    session = get_session()

    try:
        existing_count = session.query(Movie).count()
        if existing_count > 0:
            return

        movies_data = [
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

        for movie_data in movies_data:
            movie = Movie(**movie_data)
            session.add(movie)

        session.commit()

    finally:
        session.close()


# ============================================================================
# CHALLENGE 1 - DONE FOR STUDENTS
# ============================================================================

def load_movies():
    """Load ALL movies from the database."""
    session = get_session()

    try:
        movies = session.query(Movie).all()
        return [movie.to_dict() for movie in movies]
    finally:
        session.close()


# ============================================================================
# CHALLENGE 2 - SOLUTION
# ============================================================================

def get_movie_by_id(movie_id):
    """
    Find a single movie by its ID.

    CHALLENGE 2 - SOLUTION
    """
    session = get_session()

    try:
        # Query the movie by ID
        movie = session.query(Movie).filter(Movie.id == movie_id).first()

        # Check if movie exists
        if movie is None:
            return None

        # Convert to dictionary and return
        return movie.to_dict()

    finally:
        session.close()


# ============================================================================
# CHALLENGE 3 - SOLUTION
# ============================================================================

def add_review(movie_id, review):
    """
    Save a new review for a movie.

    CHALLENGE 3 - SOLUTION
    """
    session = get_session()

    try:
        # Create a new Review object
        new_review = Review(
            movie_id=movie_id,
            reviewer_name=review["name"],
            rating=review["rating"],
            comment=review["comment"]
        )

        # Add to session and commit
        session.add(new_review)
        session.commit()

    finally:
        session.close()


# ============================================================================
# CHALLENGE 4 - SOLUTION
# ============================================================================

def get_average_rating(movie_id):
    """
    Calculate the average star rating for a movie.

    CHALLENGE 4 - SOLUTION
    """
    # Get the movie
    movie = get_movie_by_id(movie_id)

    # Check if movie exists
    if movie is None:
        return 0

    # Get reviews
    reviews = movie.get("reviews", [])

    # If no reviews, return 0
    if len(reviews) == 0:
        return 0

    # Calculate total
    total = 0
    for review in reviews:
        total = total + review["rating"]

    # Calculate and round average
    average = total / len(reviews)
    return round(average, 1)


# ============================================================================
# CHALLENGE 5 - SOLUTION
# ============================================================================

def search_movies(query):
    """
    Search for movies by title.

    CHALLENGE 5 - SOLUTION
    """
    # If empty query, return all movies
    if query == "":
        return load_movies()

    # Load all movies
    movies = load_movies()

    # Case-insensitive search
    query_lower = query.lower()
    results = []

    for movie in movies:
        if query_lower in movie["title"].lower():
            results.append(movie)

    return results


# ============================================================================
# CHALLENGE 6 - SOLUTION
# ============================================================================

def get_top_rated_movies(limit=5):
    """
    Get the top rated movies based on average review ratings.

    CHALLENGE 6 - SOLUTION
    """
    # Get all movies
    movies = load_movies()
    rated_movies = []

    # Calculate ratings for each movie
    for movie in movies:
        rating = get_average_rating(movie["id"])

        # Only include movies with reviews
        if rating > 0:
            movie["avg_rating"] = rating
            rated_movies.append(movie)

    # Sort by rating (highest first)
    sorted_movies = sorted(rated_movies, key=lambda m: m["avg_rating"], reverse=True)

    # Return only top 'limit' movies
    return sorted_movies[:limit]


# ============================================================================
# CHALLENGE 7 - SOLUTION (BONUS)
# ============================================================================

def get_movies_by_genre(genre):
    """
    Get all movies that match a specific genre.

    CHALLENGE 7 - BONUS SOLUTION
    """
    movies = load_movies()

    if genre == "":
        return movies

    genre_lower = genre.lower()
    results = []

    for movie in movies:
        if movie["genre"].lower() == genre_lower:
            results.append(movie)

    return results


# ============================================================================
# CHALLENGE 8 - SOLUTION (BONUS)
# ============================================================================

def count_reviews(movie_id):
    """
    Count how many reviews a movie has.

    CHALLENGE 8 - BONUS SOLUTION
    """
    movie = get_movie_by_id(movie_id)
    if movie is None:
        return 0
    return len(movie.get("reviews", []))


# ============================================================================
# CHALLENGE 9 - SOLUTION (BONUS)
# ============================================================================

def get_all_genres():
    """
    Get a list of all unique genres in the database.

    CHALLENGE 9 - BONUS SOLUTION
    """
    movies = load_movies()
    genres = []

    for movie in movies:
        if movie["genre"] not in genres:
            genres.append(movie["genre"])

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
    session = get_session()

    try:
        # Find the review
        review = session.query(Review).filter(Review.id == review_id).first()

        # Delete if exists
        if review:
            session.delete(review)
            session.commit()

    finally:
        session.close()


# ============================================================================
# INITIALIZATION
# ============================================================================

create_tables()
seed_movies()
