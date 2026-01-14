# Workshop Slides Outline

Use this to create your presentation slides.

---

## Slide 1: Title
**Build Your First Project**
Movie Review App Workshop

Accenture x BTEC Students

---

## Slide 2: What We're Building
[Screenshot of completed app]

A Letterboxd-style movie review app where you can:
- Browse movies
- View movie details
- Write reviews
- Rate movies 1-5 stars
- Search for movies

---

## Slide 3: Tech Stack

| Tool | What It Does |
|------|-------------|
| **Python** | Our programming language |
| **FastAPI** | Turns Python into a website |
| **HTML/CSS** | Makes it look nice |
| **Replit** | Where we write and run code |

---

## Slide 4: How Web Apps Work

```
[Browser] → Request → [Server (FastAPI)] → [Database (JSON)]
                    ←  Response  ←
```

1. You type a URL
2. Server finds the right code to run
3. Code gets data from database
4. Server sends back a web page

---

## Slide 5: Project Structure

```
movie-review-app/
├── main.py          ← Our routes (URLs)
├── database.py      ← Talks to data
├── templates/       ← HTML pages
├── static/          ← CSS styles
└── data/movies.json ← Our movie data
```

---

## Slide 6: Let's Look at the Code

**database.py** - Functions to:
- Load movies
- Find a movie by ID
- Add a review
- Calculate average rating
- Search movies

**main.py** - Routes for:
- Home page (/)
- Movie detail (/movie/1)
- Add review (/movie/1/review)
- Search (/search?q=batman)

---

## Slide 7: Your First Challenge

```python
def get_movie_by_id(movie_id):
    movies = load_movies()
    # TODO: Loop through movies
    # Find the one with matching ID
    # Return it!
    pass
```

Hint: Use a `for` loop and `if` statement

---

## Slide 8: Replit Setup

1. Go to **replit.com**
2. Sign up / Log in
3. Create new "Python" Repl
4. Upload our project files
5. Click **Run**

Your mentor will help you!

---

## Slide 9: Challenge Progression

| Challenge | What You'll Build |
|-----------|------------------|
| 1-3 | Movies display on home & detail pages |
| 4-5 | Users can submit reviews |
| 6-7 | Average ratings appear |
| 8-9 | Search works |
| Bonus | Sorting, filtering, and more! |

---

## Slide 10: Tips for Success

- **Read the hints** - They're there to help!
- **Test often** - Save → Run → Check browser
- **Ask mentors** - That's what they're here for
- **Help each other** - Teaching helps you learn

---

## Slide 11: Python Basics Refresher

```python
# Variables
name = "Batman"
rating = 5

# Lists
movies = ["Batman", "Spider-Man", "Avatar"]

# Dictionaries
movie = {
    "title": "Batman",
    "year": 2022
}
# Access: movie["title"] → "Batman"

# Loops
for movie in movies:
    print(movie)
```

---

## Slide 12: Let's Go!

1. Open Replit
2. Get set up with your mentor
3. Start Challenge 1
4. Have fun building!

**Questions?** Ask your mentor!

---

## Slide 13: Wrap Up (End of Session)

You built a web app!

Skills you used today:
- Python programming
- Web development
- Working with data
- Problem solving

This is what real developers do every day.

---

## Slide 14: What's Next?

Want to keep learning?
- **freeCodeCamp.org** - Free coding courses
- **Codecademy** - Interactive Python
- **The Odin Project** - Full web dev curriculum

Keep your Replit project - it's yours!
