# Student Challenge Guide

## How This Works

All your challenges are in one file: `database.py`

Open it and look for the `TODO` comments. Complete each challenge in order!

**This app uses SQLite** - a real database that stores data in a file called `movies.db`.

---

## Challenge 1: Load Movies (DONE!)
**Already completed for you!**

Look at the `load_movies()` function to see how it works. It shows you:
- How to connect to a SQLite database
- How to run a SELECT query
- How to convert results to dictionaries

Use it as a reference for the other challenges!

---

## Challenge 2: Find a Movie by ID
**Difficulty:** Easy | **Time:** 10 mins

### Goal
When someone clicks a movie card, we need to find that specific movie's data.

### The Function
```python
def get_movie_by_id(movie_id):
    # Your code here!
    pass
```

### What to Do
1. Create a connection: `connection = get_connection()`
2. Get a cursor: `cursor = connection.cursor()`
3. Run the SELECT query: `cursor.execute("SELECT * FROM movies WHERE id = ?", (movie_id,))`
4. Get ONE result: `row = cursor.fetchone()`
5. Check if movie was found: `if row is None: return None`
6. Convert to dictionary: `movie = dict(row)`
7. Add reviews: `movie["reviews"] = get_reviews_for_movie(movie_id)`
8. Close connection: `connection.close()`
9. Return the movie!

### Hints
```python
connection = get_connection()
cursor = connection.cursor()

cursor.execute("SELECT * FROM movies WHERE id = ?", (movie_id,))
row = cursor.fetchone()

if row is None:
    connection.close()
    return None

movie = dict(row)
movie["reviews"] = get_reviews_for_movie(movie_id)

connection.close()
return movie
```

### Test It
Click on any movie poster. The movie detail page should load with the correct title, poster, and plot.

---

## Challenge 3: Save a Review
**Difficulty:** Medium | **Time:** 15 mins

### Goal
When someone submits the review form, save their review to the database!

### The Function
```python
def add_review(movie_id, review):
    # Your code here!
    pass
```

### What to Do
1. Create a connection: `connection = get_connection()`
2. Get a cursor: `cursor = connection.cursor()`
3. Run the INSERT query with the review data
4. **COMMIT the changes**: `connection.commit()` (very important!)
5. Close connection: `connection.close()`

### Hints
```python
connection = get_connection()
cursor = connection.cursor()

cursor.execute("""
    INSERT INTO reviews (movie_id, reviewer_name, rating, comment)
    VALUES (?, ?, ?, ?)
""", (movie_id, review["name"], review["rating"], review["comment"]))

connection.commit()  # Don't forget this!
connection.close()
```

### Test It
1. Click a movie to open its detail page
2. Fill in your name, select stars, write a comment
3. Click "Submit Review"
4. Your review should appear below the form!

---

## Challenge 4: Calculate Average Rating
**Difficulty:** Medium | **Time:** 15 mins

### Goal
Show the average star rating based on all reviews.

### The Function
```python
def get_average_rating(movie_id):
    # Your code here!
    return 0
```

### What to Do
1. Get reviews: `reviews = get_reviews_for_movie(movie_id)`
2. If no reviews (length is 0), return `0`
3. Add up all the ratings using a loop
4. Divide total by number of reviews
5. Use `round(average, 1)` to round to 1 decimal place

### Hints
```python
reviews = get_reviews_for_movie(movie_id)

if len(reviews) == 0:
    return 0

total = 0
for review in reviews:
    total = total + review["rating"]

average = total / len(reviews)
return round(average, 1)
```

### Test It
1. Add a few reviews with different star ratings
2. The star display should update to show the average
3. The rating number (like "4.2") should be accurate

---

## Challenge 5: Search Movies
**Difficulty:** Easy | **Time:** 10 mins

### Goal
Make the search bar work!

### The Function
```python
def search_movies(query):
    # Your code here!
    return load_movies()
```

### What to Do
1. If query is empty, return all movies: `return load_movies()`
2. Load all movies: `movies = load_movies()`
3. Convert query to lowercase: `query.lower()`
4. Loop through movies
5. Check if query is in the movie title (also lowercase)
6. Add matching movies to a results list
7. Return the results

### Hints
```python
if query == "":
    return load_movies()

movies = load_movies()
query_lower = query.lower()
results = []

for movie in movies:
    if query_lower in movie["title"].lower():
        results.append(movie)

return results
```

### Test It
- Type "dark" - should show "The Dark Knight"
- Type "SPIDER" - should show "Spider-Man: Into the Spider-Verse"
- Type "xyz" - should show "No movies found"

---

## Challenge 6: Top 5 Highest Rated
**Difficulty:** Medium | **Time:** 15 mins

### Goal
Show the user's top 5 highest-rated movies on the home page!

### The Function
```python
def get_top_rated_movies(limit=5):
    # Your code here!
    return []
```

### What to Do
1. Get all movies: `movies = load_movies()`
2. Create an empty list for movies with ratings
3. Loop through each movie
4. Get the average rating using `get_average_rating(movie["id"])`
5. Only include movies that have reviews (rating > 0)
6. Add the rating to the movie: `movie["avg_rating"] = rating`
7. Append the movie to your list
8. Sort the list by rating (highest first)
9. Return only the first `limit` movies

### Hints
```python
movies = load_movies()
rated_movies = []

for movie in movies:
    rating = get_average_rating(movie["id"])
    if rating > 0:
        movie["avg_rating"] = rating
        rated_movies.append(movie)

# Sort by rating, highest first
sorted_movies = sorted(rated_movies, key=lambda m: m["avg_rating"], reverse=True)

# Return only the top 'limit' movies
return sorted_movies[:limit]
```

### Test It
1. First, add reviews to a few movies with different ratings
2. Go back to the home page
3. You should see a "Top 5 Highest Rated" section appear
4. Movies should be ranked from highest to lowest rating

---

# BONUS CHALLENGES!

Finished the main challenges? Try these bonus ones!

---

## Challenge 7: Filter by Genre (BONUS)
**Difficulty:** Easy | **Time:** 10 mins

### Goal
Get all movies of a specific genre (like "Action" or "Drama").

### The Function
```python
def get_movies_by_genre(genre):
    # Your code here!
    return load_movies()
```

### Hints
```python
movies = load_movies()

if genre == "":
    return movies

genre_lower = genre.lower()
results = []

for movie in movies:
    if movie["genre"].lower() == genre_lower:
        results.append(movie)

return results
```

---

## Challenge 8: Count Reviews (BONUS)
**Difficulty:** Easy | **Time:** 5 mins

### Goal
Count how many reviews a movie has.

### The Function
```python
def count_reviews(movie_id):
    # Your code here!
    return 0
```

### Hints
```python
reviews = get_reviews_for_movie(movie_id)
return len(reviews)
```

---

## Challenge 9: Get All Genres (BONUS)
**Difficulty:** Medium | **Time:** 10 mins

### Goal
Get a list of all unique genres (no duplicates).

### The Function
```python
def get_all_genres():
    # Your code here!
    return []
```

### Hints
```python
movies = load_movies()
genres = []

for movie in movies:
    if movie["genre"] not in genres:
        genres.append(movie["genre"])

genres.sort()
return genres
```

---

## Challenge 10: Delete a Review (BONUS)
**Difficulty:** Medium | **Time:** 10 mins

### Goal
Remove a review from the database.

### The Function
```python
def delete_review(review_id):
    # Your code here!
    pass
```

### Hints
```python
connection = get_connection()
cursor = connection.cursor()

cursor.execute("DELETE FROM reviews WHERE id = ?", (review_id,))

connection.commit()
connection.close()
```

---

## Finished Everything?

Amazing work! You've built a complete web application with a real database!

### What You Learned
- Python fundamentals (functions, loops, dictionaries)
- **SQLite database** - a real database used in production apps!
- **SQL queries** - SELECT, INSERT, DELETE
- FastAPI for web routes
- HTML templates with Jinja2
- Form handling
- Basic data processing

### Next Steps
1. Show a mentor to get your completion certificate!
2. Try adding more features to the app

---

## Quick Reference

### SQL Commands
```sql
-- Get all movies
SELECT * FROM movies

-- Get one movie by ID
SELECT * FROM movies WHERE id = 1

-- Insert a new review
INSERT INTO reviews (movie_id, reviewer_name, rating, comment)
VALUES (1, 'John', 5, 'Great movie!')

-- Delete a review
DELETE FROM reviews WHERE id = 1
```

### Database Connection Pattern
```python
# Step 1: Connect
connection = get_connection()
cursor = connection.cursor()

# Step 2: Run query
cursor.execute("SELECT * FROM movies")

# Step 3: Get results
rows = cursor.fetchall()  # All rows
row = cursor.fetchone()   # One row

# Step 4: Close
connection.close()
```

### Dictionaries (like JavaScript objects)
```python
# Create
movie = {
    "title": "Batman",
    "year": 2022
}

# Access
movie["title"]      # "Batman"
movie.get("year")   # 2022
```

### Lists (like JavaScript arrays)
```python
# Create
movies = ["Batman", "Spider-Man"]

# Loop
for movie in movies:
    print(movie)

# Add item
movies.append("Avatar")
```

### Loops
```python
# Loop through list
for movie in movies:
    print(movie["title"])

# Loop with counting
total = 0
for review in reviews:
    total = total + review["rating"]
```

### If Statements
```python
if query == "":
    return load_movies()

if len(reviews) == 0:
    return 0
```
