# Mentor Training Guide

## Overview

You'll be supporting BTEC students (complete beginners) as they build a movie review web app using HTML, CSS, and JavaScript. The app will be deployed to GitHub Pages.

**Session Duration:** 2 hours 45 minutes
**Students per room:** ~20
**Mentors per room:** 4-5 (at least one JavaScript-strong)

---

## What Changed: Static Site for GitHub Pages

The project is now **pure HTML/CSS/JavaScript** - no Python backend needed!

- **Hosting:** GitHub Pages (free, static hosting)
- **Data Storage:** localStorage (saves reviews in the browser)
- **No server required:** Just open index.html in a browser

---

## Pre-Workshop Setup (Do Before the Day!)

### 1. Familiarize Yourself
- Read through `STUDENT_CHALLENGES.md`
- Open `movie-review-app-solution/index.html` in your browser
- Try all features: browse, search, filter, add reviews
- Complete all challenges yourself so you understand the code

### 2. Test GitHub Pages Deployment
1. Create a test repo on GitHub
2. Upload the solution files
3. Enable GitHub Pages (Settings → Pages → Deploy from main)
4. Verify it works at `https://yourusername.github.io/repo-name`

### 3. Know the Common Errors
See "Common Issues" section below.

---

## Session Flow

| Time | Activity | Your Role |
|------|----------|-----------|
| 0:00-0:15 | Intro & Demo | Show the finished app, explain the goal |
| 0:15-0:30 | Code Walkthrough | Explain HTML/CSS/JS structure |
| 0:30-0:45 | Setup | Help students download/open files |
| 0:45-2:30 | Development Time | Roam, help, unblock |
| 2:30-2:45 | GitHub Pages Deploy | Help students deploy their apps |

---

## Key Concepts to Explain

### What is JavaScript?
"JavaScript makes web pages interactive. HTML is the structure, CSS is the styling, JavaScript is the behavior - what happens when you click, type, or interact."

### What is localStorage?
"It's like a mini database in your browser. We can save data there, and it stays even when you close the browser. It's how we save reviews without needing a server."

### What is an Array?
"A list of items. Like a shopping list, but for code. We use arrays to store our list of movies."

### What is .find() and .filter()?
"These are tools for searching arrays. `.find()` gives you ONE matching item. `.filter()` gives you ALL matching items."

---

## How to Help Students

### DO:
- Guide with questions: "What do you think this line does?"
- Point them to the hints in `STUDENT_CHALLENGES.md`
- Let them type the code themselves
- Use browser DevTools to debug (F12 → Console)
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

### Issue 1: Movie Modal Shows "null" or Blank
**Cause:** `getMovieById()` is not implemented or returning null

**Fix:**
```javascript
function getMovieById(id) {
    const movies = getMovies();
    return movies.find(movie => movie.id === id);
}
```

### Issue 2: Reviews Don't Save / Disappear on Refresh
**Cause:** `saveReview()` not saving to localStorage

**Fix:** Make sure they have:
```javascript
localStorage.setItem('movieReviews', JSON.stringify(reviewsMap));
```

### Issue 3: Search Shows Empty / All Movies
**Cause:** `searchMovies()` returning wrong results

**Fix:**
```javascript
function searchMovies(query) {
    const movies = getMovies();
    return movies.filter(movie =>
        movie.title.toLowerCase().includes(query.toLowerCase())
    );
}
```

### Issue 4: "Cannot read property of undefined"
**Cause:** Usually trying to access a property on null/undefined

**Fix:** Add a guard clause:
```javascript
if (!movie || !movie.reviews) {
    return 0;
}
```

### Issue 5: Stars Always Show 0 or NaN
**Cause:** `getAverageRating()` not calculating correctly

**Fix:**
```javascript
function getAverageRating(movieId) {
    const movie = getMovieById(movieId);
    if (!movie || !movie.reviews || movie.reviews.length === 0) {
        return 0;
    }
    const total = movie.reviews.reduce((sum, r) => sum + r.rating, 0);
    return total / movie.reviews.length;
}
```

### Issue 6: GitHub Pages Shows 404
**Cause:** Wrong folder structure or file names

**Fix:**
- Make sure `index.html` is in the root (not in a subfolder)
- File names are case-sensitive! `Index.html` ≠ `index.html`
- Wait 1-2 minutes for deployment

### Issue 7: CSS/JS Not Loading on GitHub Pages
**Cause:** Wrong file paths

**Fix:** Paths should be relative:
```html
<link rel="stylesheet" href="css/style.css">  ✓
<link rel="stylesheet" href="/css/style.css"> ✗
```

---

## Challenge Solutions (For Your Reference Only!)

### Challenge 2: getMovieById
```javascript
function getMovieById(id) {
    const movies = getMovies();
    return movies.find(movie => movie.id === id);
}
```

### Challenge 3: saveReview
```javascript
function saveReview(movieId, review) {
    const savedReviews = localStorage.getItem('movieReviews');
    const reviewsMap = savedReviews ? JSON.parse(savedReviews) : {};

    if (!reviewsMap[movieId]) {
        reviewsMap[movieId] = [];
    }

    reviewsMap[movieId].push(review);
    localStorage.setItem('movieReviews', JSON.stringify(reviewsMap));
}
```

### Challenge 4: getAverageRating
```javascript
function getAverageRating(movieId) {
    const movie = getMovieById(movieId);
    if (!movie || !movie.reviews || movie.reviews.length === 0) {
        return 0;
    }
    const total = movie.reviews.reduce((sum, review) => sum + review.rating, 0);
    return total / movie.reviews.length;
}
```

### Challenge 5: searchMovies
```javascript
function searchMovies(query) {
    const movies = getMovies();
    const lowerQuery = query.toLowerCase();
    return movies.filter(movie =>
        movie.title.toLowerCase().includes(lowerQuery)
    );
}
```

### Challenge 6: filterByGenre
```javascript
function filterByGenre(genre) {
    const movies = getMovies();
    if (genre === 'all') return movies;
    if (genre === 'top-rated') {
        return movies.filter(movie => getAverageRating(movie.id) >= 4);
    }
    return movies.filter(movie =>
        movie.genre.toLowerCase().includes(genre.toLowerCase())
    );
}
```

---

## GitHub Pages Deployment Guide

Help students deploy at the end of the session:

### Step 1: Create GitHub Account (if needed)
- Go to github.com
- Sign up with email

### Step 2: Create New Repository
- Click "+" → "New repository"
- Name it `movie-review-app`
- Make it Public
- Click "Create repository"

### Step 3: Upload Files
- Click "uploading an existing file"
- Drag and drop ALL files (index.html, css/, js/)
- Click "Commit changes"

### Step 4: Enable GitHub Pages
- Go to Settings → Pages
- Source: "Deploy from a branch"
- Branch: `main`, folder: `/ (root)`
- Click Save

### Step 5: Wait & Visit
- Wait 1-2 minutes
- Visit: `https://USERNAME.github.io/movie-review-app`

---

## Pacing Guide

| Time Left | Expected Progress | Action |
|-----------|------------------|--------|
| 2 hours | Setup complete | Everyone has files open |
| 1.5 hours | Challenge 2-3 | Fast students on reviews |
| 1 hour | Challenge 4 | Most have working reviews |
| 30 mins | Challenge 5 | Search working |
| 15 mins | GitHub Pages | Help everyone deploy |

**Fast students:** Point them to Challenge 6 or bonus ideas
**Struggling students:** Focus on Challenges 2-4 (core functionality)

---

## Browser DevTools Tips

Press F12 to open DevTools. Show students:

### Console Tab
- See JavaScript errors (red text)
- Test code: `getMovies()` shows all movies
- Check values: `localStorage.getItem('movieReviews')`

### Common Console Errors
- `undefined is not a function` → Function name typo
- `Cannot read property of null` → Object doesn't exist
- `Unexpected token` → Syntax error (missing bracket, comma)

---

## Questions Students Might Ask

**Q: Why use localStorage instead of a real database?**
A: "For learning! localStorage is built into every browser - no setup needed. Real apps use databases, but this teaches the same concepts."

**Q: Will my reviews disappear if I clear browser data?**
A: "Yes! localStorage is per-browser. In a real app, you'd use a server database so data persists across devices."

**Q: Can I add my own movies?**
A: "Yes! Just add more objects to the `moviesData` array in data.js. Copy the format of existing movies."

**Q: Why doesn't my code work?**
A: Check the Console (F12) for errors. The error message usually tells you what's wrong and which line.

---

## Your Checklist

### Before the Session
- [ ] Read this entire guide
- [ ] Complete all challenges yourself
- [ ] Test GitHub Pages deployment
- [ ] Have solution open in browser for reference

### During the Session
- [ ] Help with initial setup (first 15 mins critical!)
- [ ] Roam the room - don't sit at your desk
- [ ] Check on quiet students
- [ ] Watch the clock for GitHub Pages time

### After the Session
- [ ] Note any new issues for next time
- [ ] Provide feedback to Mo

---

## Emergency Contacts

If you hit a blocker:
- **Mo (Lead):** [Add contact]
- **Backlog Support:** [Add contact]

---

You've got this! Have fun! 🎬
