# Movie Review App Workshop

A hands-on workshop where BTEC students (complete beginners) build a movie review web application using **Python** and **FastAPI**.

## Workshop Overview

| Item | Details |
|------|---------|
| **Duration** | 2 hours 45 minutes |
| **Students** | ~20 per room |
| **Mentors** | 4-5 per room (at least one Python-strong) |
| **Tech Stack** | Python, FastAPI, Jinja2, JSON |
| **Tools** | VS Code, Python 3.8+ |

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
├── slides/                      # PowerPoint presentation
│   └── workshop-slides.pptx
├── movie-review-app/            # Starter code (students work here)
│   ├── main.py                  # FastAPI routes
│   ├── database.py              # Students complete TODOs here
│   ├── requirements.txt         # Python dependencies
│   ├── data/
│   │   └── movies.json          # Movie data
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

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn main:app --reload

# Visit http://127.0.0.1:8000
```

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
| Reviews disappear | `add_review` not implemented | Complete Challenge 3 |
| Rating shows 0 | `get_average_rating` not implemented | Complete Challenge 4 |
| `IndentationError` | Mixed tabs/spaces | Use consistent 4-space indentation |
| `ModuleNotFoundError` | Dependencies not installed | Run `pip install -r requirements.txt` |

## Questions?

Contact Mo (workshop lead) for any questions or issues.

---

**Built for Accenture x BTEC Students Workshop**
