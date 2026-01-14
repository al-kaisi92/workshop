# Mentor Training Guide

## Overview

You'll be supporting BTEC students (complete beginners) as they build a movie review web app using Python and FastAPI. Students will run the app locally on Replit.

**Session Duration:** 2 hours 45 minutes
**Students per room:** ~20
**Mentors per room:** 4-5 (at least one Python-strong)

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python** | Programming language |
| **FastAPI** | Web framework (handles routes) |
| **Jinja2** | HTML templating |
| **JSON** | Data storage |
| **Replit** | Online IDE (no setup needed) |

---

## Pre-Workshop Setup (Do Before the Day!)

### 1. Familiarize Yourself
- Read through `STUDENT_CHALLENGES.md`
- Open `movie-review-app-solution/` and run it
- Try all features: browse, search, add reviews
- Complete all challenges yourself so you understand the code

### 2. Test Running the App
```bash
cd movie-review-app-solution
pip install -r requirements.txt
uvicorn main:app --reload
```
Then visit: http://127.0.0.1:8000

### 3. Know the Common Errors
See "Common Issues" section below.

---

## Session Flow

| Time | Activity | Your Role |
|------|----------|-----------|
| 0:00-0:15 | Intro & Demo | Show the finished app, explain the goal |
| 0:15-0:30 | Code Walkthrough | Explain project structure |
| 0:30-0:45 | Setup | Help students get Replit running |
| 0:45-2:30 | Development Time | Roam, help, unblock |
| 2:30-2:45 | Wrap Up | Celebrate wins, next steps |

---

## Key Concepts to Explain

### What is Python?
"Python is a programming language - it's how we tell computers what to do. It's known for being readable and beginner-friendly."

### What is FastAPI?
"FastAPI is a web framework. It takes our Python code and turns it into a website. When you visit a URL like `/movie/1`, FastAPI runs the matching function."

### What is a Dictionary?
"A dictionary stores data with labels. Like a real dictionary has words and definitions, our movie dictionary has 'title', 'year', 'genre' and their values."

### What is a for loop?
"A for loop goes through a list one item at a time. If we have 8 movies, the loop runs 8 times - once for each movie."

---

## How to Help Students

### DO:
- Guide with questions: "What do you think this line does?"
- Point them to the hints in `STUDENT_CHALLENGES.md`
- Let them type the code themselves
- Use print statements to debug
- Celebrate small wins!

### DON'T:
- Type code for them (unless stuck 10+ mins)
- Give away full solutions immediately
- Make them feel bad for not knowing
- Rush through challenges

### The 3-Step Help Process:
1. **Ask:** "What are you trying to do? What error do you see?"
2. **Hint:** Point to the relevant hint in the challenge doc
3. **Show:** If still stuck, show a small example

---

## Common Issues & Solutions

### Issue 1: `None` or blank page when clicking a movie
**Cause:** `get_movie_by_id()` returning `None` or not implemented

**Fix:**
```python
def get_movie_by_id(movie_id):
    movies = load_movies()
    for movie in movies:
        if movie["id"] == movie_id:
            return movie
    return None
```

### Issue 2: Reviews don't save / disappear
**Cause:** `add_review()` not implemented

**Fix:**
```python
def add_review(movie_id, review):
    if movie_id not in reviews_storage:
        reviews_storage[movie_id] = []
    reviews_storage[movie_id].append(review)
```

### Issue 3: Rating always shows 0
**Cause:** `get_average_rating()` not calculating

**Fix:**
```python
def get_average_rating(movie_id):
    movie = get_movie_by_id(movie_id)
    if movie is None:
        return 0
    reviews = movie.get("reviews", [])
    if len(reviews) == 0:
        return 0
    total = 0
    for review in reviews:
        total = total + review["rating"]
    return round(total / len(reviews), 1)
```

### Issue 4: Search shows all movies or empty
**Cause:** `search_movies()` not filtering

**Fix:**
```python
def search_movies(query):
    movies = load_movies()
    if query == "":
        return movies
    results = []
    for movie in movies:
        if query.lower() in movie["title"].lower():
            results.append(movie)
    return results
```

### Issue 5: `IndentationError`
**Cause:** Mixed tabs and spaces, or wrong indentation level

**Fix:** Python uses indentation (4 spaces) to define code blocks. Make sure all code inside a function is indented consistently.

### Issue 6: `KeyError: 'id'`
**Cause:** Trying to access a key that doesn't exist

**Fix:** Use `.get()` method: `movie.get("id")` returns `None` instead of crashing

### Issue 7: Server won't start / Import error
**Cause:** Missing dependencies or typo in imports

**Fix:** Run `pip install -r requirements.txt` and check import statements match exactly

---

## Challenge Solutions (For Your Reference Only!)

### Challenge 2: get_movie_by_id
```python
def get_movie_by_id(movie_id):
    movies = load_movies()
    for movie in movies:
        if movie["id"] == movie_id:
            return movie
    return None
```

### Challenge 3: add_review
```python
def add_review(movie_id, review):
    if movie_id not in reviews_storage:
        reviews_storage[movie_id] = []
    reviews_storage[movie_id].append(review)
```

### Challenge 4: get_average_rating
```python
def get_average_rating(movie_id):
    movie = get_movie_by_id(movie_id)
    if movie is None:
        return 0
    reviews = movie.get("reviews", [])
    if len(reviews) == 0:
        return 0
    total = 0
    for review in reviews:
        total = total + review["rating"]
    return round(total / len(reviews), 1)
```

### Challenge 5: search_movies
```python
def search_movies(query):
    movies = load_movies()
    if query == "":
        return movies
    results = []
    for movie in movies:
        if query.lower() in movie["title"].lower():
            results.append(movie)
    return results
```

---

## Replit Setup Guide

Help students get set up:

### Step 1: Go to Replit
- Visit **replit.com**
- Sign up / Log in

### Step 2: Create New Repl
- Click "+ Create Repl"
- Choose **Python** template
- Name it `movie-review-app`

### Step 3: Upload Files
- Delete the default `main.py`
- Drag and drop all project files
- Make sure folder structure is correct:
  ```
  movie-review-app/
  ├── main.py
  ├── database.py
  ├── requirements.txt
  ├── data/
  │   └── movies.json
  ├── templates/
  │   ├── base.html
  │   ├── index.html
  │   ├── movie.html
  │   └── error.html
  └── static/
      └── css/
          └── style.css
  ```

### Step 4: Configure Replit
In the `.replit` file, set:
```
run = "uvicorn main:app --host 0.0.0.0 --port 8080"
```

### Step 5: Run
- Click the **Run** button
- Wait for dependencies to install
- A webview should open with the app!

---

## Pacing Guide

| Time Left | Expected Progress | Action |
|-----------|------------------|--------|
| 2 hours | Setup complete | Everyone has Replit running |
| 1.5 hours | Challenge 2-3 | Fast students on reviews |
| 1 hour | Challenge 3-4 | Most have working reviews |
| 30 mins | Challenge 5 | Search working |
| 15 mins | Wrap up | Celebrate, show next steps |

**Fast students:** Point them to bonus ideas (filter by genre, add movies)
**Struggling students:** Focus on Challenges 2-4 (core functionality)

---

## Debugging Tips

### Use print() statements
```python
def get_movie_by_id(movie_id):
    print(f"Looking for movie with id: {movie_id}")  # Debug line
    movies = load_movies()
    print(f"Found {len(movies)} movies")  # Debug line
    # ... rest of code
```

### Check the terminal
- Errors appear in the Replit console
- Look for the line number in the error message

### Common error messages
- `NameError: name 'x' is not defined` → Variable name typo
- `TypeError: 'NoneType'` → Function returning None unexpectedly
- `IndentationError` → Wrong spacing/tabs

---

## Questions Students Might Ask

**Q: Why use Python instead of JavaScript?**
A: "Both are great! Python is often used for backend servers and data processing. It's known for readable syntax that's great for beginners."

**Q: Do the reviews save permanently?**
A: "In this version, reviews are stored in memory and reset when the server restarts. Real apps use databases for permanent storage."

**Q: Can I add my own movies?**
A: "Yes! Just add more objects to `movies.json`. Copy the format of existing movies."

**Q: What does FastAPI do?**
A: "It connects URLs to Python functions. When you visit `/movie/1`, FastAPI runs the `movie_detail` function with `movie_id=1`."

---

## Your Checklist

### Before the Session
- [ ] Read this entire guide
- [ ] Complete all challenges yourself
- [ ] Test running the app locally
- [ ] Have solution folder ready for reference

### During the Session
- [ ] Help with initial Replit setup (first 15 mins critical!)
- [ ] Roam the room - don't sit at your desk
- [ ] Check on quiet students
- [ ] Watch the clock for pacing

### After the Session
- [ ] Note any new issues for next time
- [ ] Provide feedback to Mo

---

## Emergency Contacts

If you hit a blocker:
- **Mo (Lead):** [Add contact]
- **Backup Support:** [Add contact]

---

You've got this! Have fun! 🎬
