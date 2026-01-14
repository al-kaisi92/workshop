# Movie Review App Workshop

A hands-on workshop where BTEC students (complete beginners) build a movie review web application using **Python** and **FastAPI**.

## Workshop Overview

| Item | Details |
|------|---------|
| **Duration** | 2 hours 45 minutes |
| **Students** | ~20 per room |
| **Mentors** | 4-5 per room (at least one Python-strong) |
| **Tech Stack** | Python, FastAPI, Jinja2, JSON |
| **Platform** | Replit (online IDE) |

## What Students Will Build

A movie review app with the following features:
- Browse a catalog of movies
- Click to view movie details
- Submit reviews with star ratings (1-5)
- See average ratings calculated from reviews
- Search movies by title

## Repository Structure

```
workshop/
├── README.md                    # This file
├── MENTOR_GUIDE.md              # Detailed guide for workshop mentors
├── STUDENT_CHALLENGES.md        # Step-by-step challenges for students
├── WORKSHOP_SLIDES_OUTLINE.md   # Presentation slides outline
├── movie-review-app/            # Starter code (students work here)
│   ├── main.py                  # FastAPI routes
│   ├── database.py              # Students complete TODOs here
│   ├── requirements.txt         # Python dependencies
│   ├── data/
│   │   └── movies.json          # Movie data
│   ├── templates/               # Jinja2 HTML templates
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── movie.html
│   │   └── error.html
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
| 0:30-0:45 | Setup | Help students get Replit running |
| 0:45-2:30 | Development | Students complete challenges with mentor help |
| 2:30-2:45 | Wrap Up | Celebrate wins, share next steps |

### The Challenges

Students work through 5 challenges in `database.py`, each marked with `TODO` comments:

| Challenge | Function | Difficulty | Time |
|-----------|----------|------------|------|
| 1 | `load_movies()` | Done for them | - |
| 2 | `get_movie_by_id()` | Easy | 10 min |
| 3 | `add_review()` | Medium | 15 min |
| 4 | `get_average_rating()` | Medium | 15 min |
| 5 | `search_movies()` | Easy | 10 min |

## Key Concepts Taught

- **Python Fundamentals**: Variables, functions, loops, dictionaries
- **Lists & Dictionaries**: Storing and accessing data
- **for loops**: Iterating through collections
- **if statements**: Conditional logic
- **FastAPI basics**: Web routes and request handling
- **JSON data**: Reading and using structured data

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

## Running Locally

### Prerequisites
- Python 3.8+
- pip

### Setup
```bash
# Clone the repo
git clone git@github.com:al-kaisi92/workshop.git
cd workshop

# Run the solution
cd movie-review-app-solution
pip install -r requirements.txt
uvicorn main:app --reload

# Visit http://127.0.0.1:8000
```

### Run the starter code
```bash
cd movie-review-app
pip install -r requirements.txt
uvicorn main:app --reload
```

## Replit Setup

For the workshop, students use Replit (no local setup needed):

1. Go to **replit.com** and sign up
2. Create new **Python** Repl
3. Upload all files from `movie-review-app/`
4. In `.replit` file, set: `run = "uvicorn main:app --host 0.0.0.0 --port 8080"`
5. Click **Run**

## Workshop Materials

| Document | Audience | Purpose |
|----------|----------|---------|
| `STUDENT_CHALLENGES.md` | Students | Step-by-step coding challenges |
| `MENTOR_GUIDE.md` | Mentors | Troubleshooting, solutions, tips |
| `WORKSHOP_SLIDES_OUTLINE.md` | Presenter | Slide deck content outline |

## Common Issues

| Issue | Cause | Fix |
|-------|-------|-----|
| `None` when clicking movie | `get_movie_by_id` not implemented | Complete Challenge 2 |
| Reviews disappear | `add_review` not implemented | Complete Challenge 3 |
| Rating shows 0 | `get_average_rating` not implemented | Complete Challenge 4 |
| `IndentationError` | Mixed tabs/spaces | Use consistent 4-space indentation |

## Questions?

Contact Mo (workshop lead) for any questions or issues.

---

**Built for Accenture x BTEC Students Workshop**
