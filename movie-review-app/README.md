# CineRate - Movie Review App

A modern movie review application built with HTML, CSS, and JavaScript.

## Quick Start

### Option 1: Open Directly
Just open `index.html` in your browser!

### Option 2: Use Live Server (Recommended)
1. Install the "Live Server" extension in VS Code
2. Right-click on `index.html`
3. Select "Open with Live Server"

### Option 3: GitHub Pages
This project is designed to be deployed on GitHub Pages. Just push to your repo and enable Pages in settings!

## Project Structure

```
movie-review-app/
├── index.html      ← Main HTML page
├── css/
│   └── style.css   ← All the styling
└── js/
    ├── data.js     ← Movie data & YOUR CHALLENGES!
    └── app.js      ← App logic (already complete)
```

## Your Challenges

All your challenges are in `js/data.js`. Look for the TODO comments!

### Challenge 1: Get Movies (Already Done!)
The `getMovies()` function is complete - use it as a reference.

### Challenge 2: Find a Movie by ID
Complete `getMovieById(id)` to find a specific movie.

### Challenge 3: Save a Review
Complete `saveReview(movieId, review)` to save reviews to localStorage.

### Challenge 4: Calculate Average Rating
Complete `getAverageRating(movieId)` to calculate star ratings.

### Challenge 5: Search Movies
Complete `searchMovies(query)` to enable the search feature.

### Challenge 6: Filter by Genre (Bonus)
Complete `filterByGenre(genre)` to make the filter buttons work.

## JavaScript Concepts You'll Use

```javascript
// Arrays
const movies = [movie1, movie2, movie3];

// Find an item
const movie = movies.find(m => m.id === 5);

// Filter items
const actionMovies = movies.filter(m => m.genre.includes("Action"));

// Loop through array
for (const movie of movies) {
    console.log(movie.title);
}

// localStorage
localStorage.setItem('key', JSON.stringify(data));  // Save
const data = JSON.parse(localStorage.getItem('key'));  // Load
```

## Testing Your Code

1. **Challenge 2**: Click on any movie - it should open a modal with details
2. **Challenge 3**: Submit a review - it should appear in the reviews list
3. **Challenge 4**: After adding reviews, star ratings should update
4. **Challenge 5**: Type in the search box - movies should filter
5. **Challenge 6**: Click filter buttons - movies should filter by genre

## Need Help?

Ask a mentor! That's what they're here for.

## Deploying to GitHub Pages

1. Create a GitHub repository
2. Push your code to the `main` branch
3. Go to Settings → Pages
4. Select "Deploy from branch" → `main`
5. Your site will be live at `https://yourusername.github.io/repo-name`
