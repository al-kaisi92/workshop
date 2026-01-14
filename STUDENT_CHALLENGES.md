# Student Challenge Guide

## How This Works

All your challenges are in one file: `js/data.js`

Open it and look for the `TODO` comments. Complete each challenge in order!

---

## Challenge 1: Get Movies (DONE!)
**Already completed for you!**

Look at the `getMovies()` function to see how it works. Use it as a reference!

---

## Challenge 2: Find a Movie by ID
**Difficulty:** Easy | **Time:** 10 mins

### Goal
When someone clicks a movie card, we need to find that specific movie's data.

### The Function
```javascript
function getMovieById(id) {
    // Your code here!
}
```

### What to Do
1. Call `getMovies()` to get all movies
2. Use `.find()` to locate the movie with matching id
3. Return that movie

### Hints
```javascript
// The .find() method searches an array
const movies = getMovies();
const movie = movies.find(movie => movie.id === id);
return movie;
```

### Test It
Click on any movie poster. The modal should open showing the movie's title, poster, and plot.

---

## Challenge 3: Save a Review
**Difficulty:** Medium | **Time:** 20 mins

### Goal
When someone submits the review form, save their review so it persists!

### The Function
```javascript
function saveReview(movieId, review) {
    // Your code here!
}
```

### What to Do
1. Get existing reviews from localStorage
2. Parse the JSON (or create empty object if none)
3. Add the review to the correct movie's array
4. Save back to localStorage

### Hints
```javascript
// Get from localStorage
const savedReviews = localStorage.getItem('movieReviews');
const reviewsMap = savedReviews ? JSON.parse(savedReviews) : {};

// Make sure this movie has an array
if (!reviewsMap[movieId]) {
    reviewsMap[movieId] = [];
}

// Add the review
reviewsMap[movieId].push(review);

// Save back
localStorage.setItem('movieReviews', JSON.stringify(reviewsMap));
```

### Test It
1. Click a movie to open the modal
2. Fill in your name, select stars, write a comment
3. Click "Submit Review"
4. Your review should appear below the form!
5. Refresh the page - your review should still be there!

---

## Challenge 4: Calculate Average Rating
**Difficulty:** Medium | **Time:** 15 mins

### Goal
Show the average star rating based on all reviews.

### The Function
```javascript
function getAverageRating(movieId) {
    // Your code here!
}
```

### What to Do
1. Get the movie using `getMovieById()`
2. If no movie or no reviews, return 0
3. Add up all the ratings
4. Divide by the number of reviews
5. Return the result

### Hints
```javascript
const movie = getMovieById(movieId);

// Guard clause
if (!movie || !movie.reviews || movie.reviews.length === 0) {
    return 0;
}

// Sum all ratings
let total = 0;
for (const review of movie.reviews) {
    total = total + review.rating;
}

// Calculate average
return total / movie.reviews.length;
```

### Or use .reduce() (advanced):
```javascript
const total = movie.reviews.reduce((sum, review) => sum + review.rating, 0);
return total / movie.reviews.length;
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
```javascript
function searchMovies(query) {
    // Your code here!
}
```

### What to Do
1. Get all movies
2. Convert the query to lowercase (for case-insensitive search)
3. Filter movies where the title includes the query
4. Return the filtered list

### Hints
```javascript
const movies = getMovies();
const lowerQuery = query.toLowerCase();

return movies.filter(movie =>
    movie.title.toLowerCase().includes(lowerQuery)
);
```

### Test It
- Type "dark" → should show "The Dark Knight"
- Type "SPIDER" → should show "Spider-Man: Into the Spider-Verse"
- Type "xyz" → should show "No movies found"

---

## Challenge 6: Filter by Genre (BONUS)
**Difficulty:** Medium | **Time:** 15 mins

### Goal
Make the filter buttons work (Action, Drama, Sci-Fi, etc.)

### The Function
```javascript
function filterByGenre(genre) {
    // Your code here!
}
```

### What to Do
1. If genre is 'all', return all movies
2. If genre is 'top-rated', return movies with average rating >= 4
3. Otherwise, filter by genre name

### Hints
```javascript
if (genre === 'all') {
    return movies;
}

if (genre === 'top-rated') {
    return movies.filter(movie => getAverageRating(movie.id) >= 4);
}

return movies.filter(movie =>
    movie.genre.toLowerCase().includes(genre.toLowerCase())
);
```

### Test It
- Click "Action" → should show action movies
- Click "Animation" → should show animated movies
- Click "Top Rated" → should show movies with 4+ stars

---

## Finished Everything?

Amazing work! You've built a complete web application!

### What You Learned
- JavaScript fundamentals (functions, arrays, objects)
- Array methods (find, filter, map, reduce)
- localStorage for data persistence
- DOM manipulation
- Event handling

### Next Steps
1. Deploy to GitHub Pages (instructions in README)
2. Show a mentor to get your completion certificate!
3. Try adding more features:
   - Sort by year
   - Sort by rating
   - Add more movies
   - Change the color theme

---

## Quick Reference

### Arrays
```javascript
// Create
const nums = [1, 2, 3];

// Access
nums[0]  // 1

// Loop
for (const num of nums) { }

// Find one
nums.find(n => n > 2)  // 3

// Filter many
nums.filter(n => n > 1)  // [2, 3]

// Transform
nums.map(n => n * 2)  // [2, 4, 6]
```

### Objects
```javascript
const movie = {
    title: "Batman",
    year: 2022
};

movie.title      // "Batman"
movie["year"]    // 2022
```

### localStorage
```javascript
// Save
localStorage.setItem('key', JSON.stringify(data));

// Load
const data = JSON.parse(localStorage.getItem('key'));
```
