# Student Challenge Guide

## How This Works

All your challenges are in one file: `database.py`

Open it and look for the `TODO` comments. Complete each challenge in order!

---

## Challenge 1: Load Movies (DONE!)
**Already completed for you!**

Look at the `load_movies()` function to see how it works. Use it as a reference!

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
1. Call `load_movies()` to get all movies
2. Loop through the movies with `for movie in movies:`
3. Check if `movie["id"]` equals `movie_id`
4. If it matches, return that movie
5. If no match found, return `None`

### Hints
```python
movies = load_movies()
for movie in movies:
    if movie["id"] == movie_id:
        return movie
return None
```

### Test It
Click on any movie poster. The movie detail page should load with the correct title, poster, and plot.

---

## Challenge 3: Save a Review
**Difficulty:** Medium | **Time:** 15 mins

### Goal
When someone submits the review form, save their review!

### The Function
```python
def add_review(movie_id, review):
    # Your code here!
    pass
```

### What to Do
1. Check if `movie_id` exists in `reviews_storage`
2. If not, create an empty list: `reviews_storage[movie_id] = []`
3. Append the review: `reviews_storage[movie_id].append(review)`

### Hints
```python
if movie_id not in reviews_storage:
    reviews_storage[movie_id] = []
reviews_storage[movie_id].append(review)
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
1. Get the movie using `get_movie_by_id(movie_id)`
2. If no movie found, return `0`
3. Get the reviews: `reviews = movie.get("reviews", [])`
4. If no reviews (length is 0), return `0`
5. Add up all the ratings using a loop
6. Divide total by number of reviews
7. Use `round(average, 1)` to round to 1 decimal place

### Hints
```python
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
1. Get all movies: `movies = load_movies()`
2. If query is empty, return all movies
3. Convert query to lowercase: `query.lower()`
4. Loop through movies
5. Check if query is in the movie title (also lowercase)
6. Add matching movies to a results list
7. Return the results

### Hints
```python
movies = load_movies()

if query == "":
    return movies

query_lower = query.lower()
results = []

for movie in movies:
    if query_lower in movie["title"].lower():
        results.append(movie)

return results
```

### Test It
- Type "dark" → should show "The Dark Knight"
- Type "SPIDER" → should show "Spider-Man: Into the Spider-Verse"
- Type "xyz" → should show "No movies found"

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

## Finished Everything?

Amazing work! You've built a complete web application!

### What You Learned
- Python fundamentals (functions, loops, dictionaries)
- Reading JSON data files
- FastAPI for web routes
- HTML templates with Jinja2
- Form handling
- Basic data processing

### Next Steps
1. Show a mentor to get your completion certificate!
2. Try adding more features:
   - Filter by genre
   - Sort by year
   - Add more movies to `movies.json`

---

## Quick Reference

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
if movie_id not in reviews_storage:
    reviews_storage[movie_id] = []

if len(reviews) == 0:
    return 0
```
