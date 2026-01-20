# Workshop Slides Outline

Use this to create your presentation slides.

---

## Slide 1: Title
**Build Your First Web App**
Movie Review App Workshop

Accenture x BTEC Students

---

## Slide 2: What We're Building
[Screenshot of completed app]

A movie review app where you can:
- Browse movies
- View movie details
- Write reviews
- Rate movies 1-5 stars
- Search for movies
- See Top 5 highest-rated movies

---

## Slide 3: Tech Stack

| Tool | What It Does |
|------|-------------|
| **Python** | Our programming language |
| **FastAPI** | Turns Python into a website |
| **HTML/CSS** | Makes it look nice |
| **VS Code** | Where we write and run code |

---

## Slide 4: How Web Apps Work

```
[Browser] → Request → [Server (Python/FastAPI)] → [Data (JSON)]
                    ←  Response  ←
```

1. You type a URL
2. Server finds the right code to run
3. Code gets data from JSON file
4. Server sends back a web page

---

## Slide 5: Project Structure

```
movie-review-app/
├── main.py          ← Our routes (URLs)
├── database.py      ← Functions you'll write!
├── templates/       ← HTML pages
├── static/css/      ← Styles
└── data/movies.json ← Our movie data
```

---

## Slide 6: Python Fundamentals - Variables

Variables store information:

```python
# Text (strings) - use quotes
name = "Batman"
genre = "Action"

# Numbers (integers) - no quotes
year = 2022
rating = 5

# Decimals (floats)
average = 4.5
```

Think of variables as labelled boxes that hold data.

---

## Slide 7: Python Fundamentals - Lists

Lists hold multiple items:

```python
# Create a list
movies = ["Batman", "Spider-Man", "Avatar"]

# Access items (starts at 0!)
movies[0]  # "Batman"
movies[1]  # "Spider-Man"

# Add an item
movies.append("Inception")

# How many items?
len(movies)  # 4
```

---

## Slide 8: Python Fundamentals - Dictionaries

Dictionaries store data with labels (like a real dictionary!):

```python
# Create a dictionary
movie = {
    "title": "The Dark Knight",
    "year": 2008,
    "genre": "Action"
}

# Access values using the label (key)
movie["title"]  # "The Dark Knight"
movie["year"]   # 2008

# Safely get a value (won't crash if missing)
movie.get("rating", 0)  # Returns 0 if no rating
```

---

## Slide 9: Python Fundamentals - For Loops

Loops let you repeat code for each item:

```python
movies = ["Batman", "Spider-Man", "Avatar"]

# Do something for each movie
for movie in movies:
    print(movie)

# Output:
# Batman
# Spider-Man
# Avatar
```

The loop runs 3 times - once for each movie!

---

## Slide 10: Python Fundamentals - If Statements

If statements make decisions:

```python
rating = 5

if rating > 4:
    print("Great movie!")
elif rating > 2:
    print("It's okay")
else:
    print("Not great")

# Check equality with ==
if movie["title"] == "Batman":
    print("Found it!")
```

---

## Slide 11: Python Fundamentals - Functions

Functions are reusable blocks of code:

```python
# Define a function
def greet(name):
    return "Hello, " + name + "!"

# Call the function
message = greet("Mo")
print(message)  # "Hello, Mo!"
```

Functions can take inputs and give outputs.

---

## Slide 12: VS Code Setup

1. Open **VS Code**
2. Open the `movie-review-app` folder
3. Open Terminal (Ctrl + `)
4. Run: `pip install -r requirements.txt`
5. Run: `uvicorn main:app --reload`
6. Open browser: **http://127.0.0.1:8000**

Your mentor will help you!

---

## Slide 13: Let's Look at the App Code

**database.py** - Functions to complete:
- Load movies (done for you!)
- Find a movie by ID
- Add a review
- Calculate average rating
- Search movies
- Get top 5 rated movies

**main.py** - Routes (already built):
- Home page (/)
- Movie detail (/movie/1)
- Search (/search?q=batman)

---

## Slide 14: Challenge Progression

| Challenge | What You'll Build | Difficulty |
|-----------|------------------|------------|
| 1 | Load movies | Done for you! |
| 2 | Find a movie by ID | Easy |
| 3 | Save reviews | Medium |
| 4 | Calculate average ratings | Medium |
| 5 | Search for movies | Easy |
| 6 | Show Top 5 highest-rated | Medium |

---

## Slide 15: Challenge 1 - Load Movies (Done For You!)

This one is already complete - let's understand it:

```python
def load_movies():
    # Open the JSON file
    with open("data/movies.json", "r") as file:
        movies = json.load(file)

    # Return the list of movies
    return movies
```

**What it does:**
1. Opens the `movies.json` file
2. Reads all the movie data
3. Returns it as a list of dictionaries

This is how we get our movie data into the app!

---

## Slide 16: Understanding the Movie Data

Each movie in `movies.json` looks like this:

```python
{
    "id": 1,
    "title": "The Dark Knight",
    "year": 2008,
    "genre": "Action",
    "plot": "Batman fights the Joker...",
    "poster": "https://image-url.com/poster.jpg"
}
```

We have 8 movies to work with!

---

## Slide 17: Challenge 2 - Find a Movie by ID

**Goal:** When someone clicks a movie, find that specific movie.

```python
def get_movie_by_id(movie_id):
    # TODO: Your code here!
    pass
```

**What you need to do:**
1. Get all movies using `load_movies()`
2. Loop through each movie
3. Check if the movie's ID matches
4. Return the matching movie

---

## Slide 18: Challenge 2 - Hints

```python
def get_movie_by_id(movie_id):
    # Step 1: Get all movies
    movies = load_movies()

    # Step 2: Loop through each movie
    for movie in movies:
        # Step 3: Check if ID matches
        if movie["id"] == movie_id:
            # Step 4: Return it!
            return movie

    # Step 5: If not found, return None
    return None
```

---

## Slide 19: Challenge 3 - Save a Review

**Goal:** When someone submits a review, save it!

```python
def add_review(movie_id, review):
    # TODO: Your code here!
    pass
```

**What you need to do:**
1. Check if this movie already has reviews stored
2. If not, create an empty list for it
3. Add the new review to the list

---

## Slide 20: Challenge 4 - Calculate Average Rating

**Goal:** Show the average star rating from all reviews.

```python
def get_average_rating(movie_id):
    # TODO: Your code here!
    return 0
```

**What you need to do:**
1. Get the movie and its reviews
2. Add up all the ratings
3. Divide by the number of reviews
4. Return the average

---

## Slide 21: Challenge 5 - Search Movies

**Goal:** Make the search bar work!

```python
def search_movies(query):
    # TODO: Your code here!
    return load_movies()
```

**What you need to do:**
1. Get all movies
2. Loop through and check if the title contains the search term
3. Return only the matching movies

---

## Slide 22: Challenge 6 - Top 5 Highest Rated

**Goal:** Show the 5 movies with the best ratings!

```python
def get_top_rated_movies(limit=5):
    # TODO: Your code here!
    return []
```

**What you need to do:**
1. Get all movies
2. Find movies that have reviews
3. Sort them by rating (highest first)
4. Return the top 5

---

## Slide 23: The Challenge Pattern

Most challenges follow this pattern:

```python
def function_name(input):
    # 1. Get the data you need
    movies = load_movies()

    # 2. Loop through items
    for movie in movies:
        # 3. Check a condition
        if movie["id"] == input:
            # 4. Return a result
            return movie

    # 5. Handle "not found" case
    return None
```

---

## Slide 24: Tips for Success

- **Read the hints** - They're in STUDENT_CHALLENGES.md!
- **Test often** - Save → Check browser
- **Use print()** - Add `print(variable)` to see values
- **Ask mentors** - That's what they're here for
- **Help each other** - Teaching helps you learn

---

## Slide 25: Common Mistakes to Avoid

```python
# WRONG: Using = instead of ==
if rating = 5:      # This assigns, doesn't compare!

# RIGHT: Use == to compare
if rating == 5:     # This checks if equal

# WRONG: Forgetting to return
def get_movie(id):
    for movie in movies:
        if movie["id"] == id:
            movie  # Oops! Nothing returned

# RIGHT: Use return keyword
def get_movie(id):
    for movie in movies:
        if movie["id"] == id:
            return movie  # This sends it back!
```

---

## Slide 26: Let's Go!

1. Open VS Code
2. Get set up with your mentor
3. Open `database.py`
4. Read Challenge 1 to understand the code
5. Start Challenge 2
6. Have fun building!

**Questions?** Ask your mentor!

---

## Slide 27: Wrap Up (End of Session)

You built a web app with Python!

Skills you used today:
- Python programming (loops, dictionaries, functions)
- Web development with FastAPI
- Working with JSON data
- Problem solving & debugging

This is what real developers do every day.

---

## Slide 28: What's Next?

Want to keep learning?
- **freeCodeCamp.org** - Free coding courses
- **Codecademy** - Interactive Python
- **Real Python** - Python tutorials
- **W3Schools** - Web development basics

Keep your project - add it to your portfolio!
