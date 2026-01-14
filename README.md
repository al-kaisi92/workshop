# Movie Review App Workshop

A hands-on workshop where BTEC students (complete beginners) build a movie review web application using HTML, CSS, and JavaScript, then deploy it to GitHub Pages.

## Workshop Overview

| Item | Details |
|------|---------|
| **Duration** | 2 hours 45 minutes |
| **Students** | ~20 per room |
| **Mentors** | 4-5 per room (at least one JavaScript-strong) |
| **Tech Stack** | HTML, CSS, JavaScript (no backend) |
| **Deployment** | GitHub Pages (free static hosting) |
| **Data Storage** | localStorage (browser-based) |

## What Students Will Build

A Letterboxd-style movie review app with the following features:
- Browse a catalog of movies
- Click to view movie details in a modal
- Submit reviews with star ratings (1-5)
- See average ratings calculated from reviews
- Search movies by title
- Filter by genre and top-rated

## Repository Structure

```
workshop/
├── README.md                    # This file
├── MENTOR_GUIDE.md              # Detailed guide for workshop mentors
├── STUDENT_CHALLENGES.md        # Step-by-step challenges for students
├── WORKSHOP_SLIDES_OUTLINE.md   # Presentation slides outline
├── movie-review-app/            # Starter code (students work here)
│   ├── index.html
│   ├── css/
│   │   └── style.css
│   └── js/
│       ├── app.js
│       └── data.js              # Students complete TODOs here
├── movie-review-app-solution/   # Complete working solution
└── docs/                        # GitHub Pages site
```

## How The Workshop Works

### Session Flow

| Time | Activity | Description |
|------|----------|-------------|
| 0:00-0:15 | Intro & Demo | Show the finished app, explain goals |
| 0:15-0:30 | Code Walkthrough | Explain HTML/CSS/JS structure |
| 0:30-0:45 | Setup | Help students download and open files |
| 0:45-2:30 | Development | Students complete challenges with mentor help |
| 2:30-2:45 | Deployment | Help students deploy to GitHub Pages |

### The Challenges

Students work through 6 challenges in `js/data.js`, each marked with `TODO` comments:

| Challenge | Function | Difficulty | Time |
|-----------|----------|------------|------|
| 1 | `getMovies()` | Done for them | - |
| 2 | `getMovieById()` | Easy | 10 min |
| 3 | `saveReview()` | Medium | 20 min |
| 4 | `getAverageRating()` | Medium | 15 min |
| 5 | `searchMovies()` | Easy | 10 min |
| 6 | `filterByGenre()` | Medium (Bonus) | 15 min |

## Key Concepts Taught

- **JavaScript Fundamentals**: Variables, functions, arrays, objects
- **Array Methods**: `.find()`, `.filter()`, `.reduce()`, `.map()`
- **localStorage**: Browser-based data persistence
- **DOM Manipulation**: Updating the page dynamically
- **Event Handling**: Responding to user interactions

## For Mentors

### Before the Workshop

1. **Read** `MENTOR_GUIDE.md` thoroughly
2. **Complete** all challenges yourself
3. **Test** GitHub Pages deployment with a test repo
4. **Review** common issues section in mentor guide

### During the Workshop

- **DO**: Guide with questions, point to hints, let students type
- **DON'T**: Type code for them, give away solutions immediately

### The 3-Step Help Process

1. **Ask**: "What are you trying to do? What error do you see?"
2. **Hint**: Point to the relevant hint in `STUDENT_CHALLENGES.md`
3. **Show**: If still stuck (10+ mins), show a small example

## GitHub Pages Deployment

### For Students (End of Session)

1. Create GitHub account (if needed)
2. Create new repository named `movie-review-app`
3. Upload all files (index.html, css/, js/)
4. Go to Settings → Pages → Deploy from branch `main`
5. Wait 1-2 minutes
6. Visit: `https://USERNAME.github.io/movie-review-app`

### Common Deployment Issues

| Issue | Cause | Fix |
|-------|-------|-----|
| 404 error | Wrong file structure | Ensure `index.html` is in root |
| CSS not loading | Wrong paths | Use relative paths: `href="css/style.css"` |
| Page not updating | Cache | Hard refresh (Ctrl+Shift+R) |

## Local Development

No build tools required! Simply:

```bash
# Clone the repo
git clone git@github.com:al-kaisi92/workshop.git

# Open the starter app in your browser
open movie-review-app/index.html

# Or open the solution
open movie-review-app-solution/index.html
```

## Workshop Materials

| Document | Audience | Purpose |
|----------|----------|---------|
| `STUDENT_CHALLENGES.md` | Students | Step-by-step coding challenges |
| `MENTOR_GUIDE.md` | Mentors | Troubleshooting, solutions, tips |
| `WORKSHOP_SLIDES_OUTLINE.md` | Presenter | Slide deck content outline |

## Browser DevTools

Essential for debugging. Press F12 to open:

- **Console Tab**: See JavaScript errors (red text)
- **Test code**: Type `getMovies()` to see all movies
- **Check storage**: `localStorage.getItem('movieReviews')`

## Questions?

Contact Mo (workshop lead) for any questions or issues.

---

**Built for Accenture x BTEC Students Workshop**
