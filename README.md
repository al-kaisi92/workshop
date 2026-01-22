# Movie Review App Workshop

A hands-on workshop where BTEC students (complete beginners) build a movie review web application using **Python**, **FastAPI**, and **SQLite**.

## Workshop Overview

| Item | Details |
|------|---------|
| **Duration** | 2 hours 45 minutes |
| **Students** | ~20 per room |
| **Mentors** | 4-5 per room (at least one Python-strong) |
| **Tech Stack** | Python, FastAPI, Jinja2, SQLAlchemy, SQLite |
| **Tools** | VS Code, Python 3.8+ |

## What Students Will Build

A movie review app with the following features:
- Browse a catalog of 12 movies
- Click to view movie details
- Submit reviews with star ratings (1-5)
- See average ratings calculated from reviews
- Search movies by title
- View Top 5 highest-rated movies
- **NEW**: All data stored in a real SQLite database!

## Repository Structure

```
workshop/
├── README.md                    # This file
├── MENTOR_GUIDE.md              # Detailed guide for workshop mentors
├── STUDENT_CHALLENGES.md        # Step-by-step challenges for students
├── Product Backlog - Movie Review App(Backlog).csv  # BTEC product backlog
├── slides/                      # PowerPoint presentation
│   └── workshop-slides.pptx
├── movie-review-app/            # Starter code (students work here)
│   ├── main.py                  # FastAPI routes (fully commented)
│   ├── database.py              # Students complete TODOs here (10 challenges)
│   ├── requirements.txt         # Python dependencies
│   ├── templates/               # Jinja2 HTML templates
│   └── static/css/
│       └── style.css
├── movie-review-app-solution/   # Complete working solution
└── docs/                        # GitHub Pages site
```

## How The Workshop Works

### Session Flow

| Time | Activity | Description |
|------|----------|-------------|
| 0:00-0:15 | Intro & Demo | Show the finished app, explain goals |
| 0:15-0:30 | Code Walkthrough | Explain project structure |
| 0:30-0:45 | Setup | Help students set up VS Code and Python |
| 0:45-2:30 | Development | Students complete challenges with mentor help |
| 2:30-2:45 | Wrap Up | Celebrate wins, share next steps |

### The Challenges

Students work through challenges in `database.py`, each marked with `TODO` comments:

#### Core Challenges (Required)

| Challenge | Function | Difficulty | Time |
|-----------|----------|------------|------|
| 1 | `load_movies()` | Done for them | - |
| 2 | `get_movie_by_id()` | Easy | 10 min |
| 3 | `add_review()` | Medium | 15 min |
| 4 | `get_average_rating()` | Medium | 15 min |
| 5 | `search_movies()` | Easy | 10 min |
| 6 | `get_top_rated_movies()` | Medium | 15 min |

#### Bonus Challenges (For Fast Learners)

| Challenge | Function | Difficulty | Time |
|-----------|----------|------------|------|
| 7 | `get_movies_by_genre()` | Easy | 10 min |
| 8 | `count_reviews()` | Easy | 5 min |
| 9 | `get_all_genres()` | Medium | 10 min |
| 10 | `delete_review()` | Medium | 10 min |

## Key Concepts Taught

- **Python Fundamentals**: Variables, functions, loops, dictionaries
- **SQLAlchemy ORM**: Industry-standard database library for Python
- **Database Models**: Representing tables as Python classes
- **Sessions**: Managing database connections
- **Lists & Dictionaries**: Storing and accessing data
- **for loops**: Iterating through collections
- **if statements**: Conditional logic
- **Sorting**: Using `sorted()` with custom keys
- **FastAPI basics**: Web routes and request handling

## For Mentors

### Before the Workshop

1. **Read** `MENTOR_GUIDE.md` thoroughly
2. **Complete** all challenges yourself
3. **Test** running the app locally
4. **Review** common issues section in mentor guide

### During the Workshop

- **DO**: Guide with questions, point to hints, let students type
- **DON'T**: Type code for them, give away solutions immediately

### The 3-Step Help Process

1. **Ask**: "What are you trying to do? What error do you see?"
2. **Hint**: Point to the relevant hint in `STUDENT_CHALLENGES.md`
3. **Show**: If still stuck (10+ mins), show a small example

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- VS Code (with Python extension)
- pip (Python package manager)

### Running the App

```bash
# Clone the repo
git clone git@github.com:al-kaisi92/workshop.git
cd workshop/movie-review-app

# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn main:app --reload

# Visit http://127.0.0.1:8000
```

**Note**: When you first run the app, it will automatically:
1. Create a `movies.db` SQLite database file
2. Create the `movies` and `reviews` tables
3. Seed the database with 12 movies

### VS Code Setup for Students

1. Install [VS Code](https://code.visualstudio.com/)
2. Install [Python](https://www.python.org/downloads/)
3. Install the Python extension in VS Code
4. Open the `movie-review-app` folder
5. Open terminal (Ctrl+`) and run the commands above

## Workshop Materials

| Document | Audience | Purpose |
|----------|----------|---------|
| `STUDENT_CHALLENGES.md` | Students | Step-by-step coding challenges |
| `MENTOR_GUIDE.md` | Mentors | Troubleshooting, solutions, tips |
| `slides/workshop-slides.pptx` | Presenter | PowerPoint presentation |

## Common Issues

| Issue | Cause | Fix |
|-------|-------|-----|
| `None` when clicking movie | `get_movie_by_id` not implemented | Complete Challenge 2 |
| Reviews disappear on refresh | `add_review` not committing | Add `connection.commit()` in Challenge 3 |
| Rating shows 0 | `get_average_rating` not implemented | Complete Challenge 4 |
| Top 5 not showing | `get_top_rated_movies` not implemented or no reviews added | Complete Challenge 6, add some reviews first |
| `IndentationError` | Mixed tabs/spaces | Use consistent 4-space indentation |
| `ModuleNotFoundError` | Dependencies not installed | Run `pip install -r requirements.txt` |
| `movies.db` gets corrupted | Database issues | Delete `movies.db` and restart the app |

## Movies Included

The app comes pre-seeded with 12 popular movies:
1. The Dark Knight (2008) - Action
2. Inception (2010) - Sci-Fi
3. Spider-Man: Into the Spider-Verse (2018) - Animation
4. The Shawshank Redemption (1994) - Drama
5. Interstellar (2014) - Sci-Fi
6. The Lion King (1994) - Animation
7. Avengers: Endgame (2019) - Action
8. Parasite (2019) - Drama
9. The Matrix (1999) - Sci-Fi
10. Forrest Gump (1994) - Drama
11. Toy Story (1995) - Animation
12. Pulp Fiction (1994) - Crime
