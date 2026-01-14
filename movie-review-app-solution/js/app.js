/**
 * CineRate - Movie Review App
 * Main Application Logic
 */

// DOM Elements
const movieGrid = document.getElementById('movieGrid');
const noResults = document.getElementById('noResults');
const searchInput = document.getElementById('searchInput');
const movieModal = document.getElementById('movieModal');
const modalBody = document.getElementById('modalBody');
const closeModal = document.getElementById('closeModal');
const movieCount = document.getElementById('movieCount');
const filterBtns = document.querySelectorAll('.filter-btn');

// Current state
let currentFilter = 'all';

/**
 * Initialize the app
 */
function init() {
    renderMovies(getMovies());
    setupEventListeners();
}

/**
 * Set up all event listeners
 */
function setupEventListeners() {
    // Search
    searchInput.addEventListener('input', handleSearch);

    // Filter buttons
    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => handleFilter(btn));
    });

    // Modal close
    closeModal.addEventListener('click', closeMovieModal);
    document.querySelector('.modal-backdrop').addEventListener('click', closeMovieModal);

    // Close modal on Escape key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') closeMovieModal();
    });
}

/**
 * Render movies to the grid
 */
function renderMovies(movies) {
    movieCount.textContent = movies.length;

    if (movies.length === 0) {
        movieGrid.innerHTML = '';
        noResults.classList.remove('hidden');
        return;
    }

    noResults.classList.add('hidden');

    movieGrid.innerHTML = movies.map(movie => {
        const avgRating = getAverageRating(movie.id);
        return `
            <article class="movie-card" onclick="openMovieModal(${movie.id})">
                <div class="movie-poster">
                    <img src="${movie.poster}" alt="${movie.title}" loading="lazy">
                    <div class="movie-overlay">
                        <div class="movie-overlay-content">
                            <span class="genre">${movie.genre}</span>
                            <span class="view-btn">View Details →</span>
                        </div>
                    </div>
                </div>
                <div class="movie-info">
                    <h3 class="movie-title">${movie.title}</h3>
                    <div class="movie-meta">
                        <span class="movie-year">${movie.year}</span>
                        <div class="movie-rating">
                            <span class="star">★</span>
                            <span class="rating-value">${avgRating > 0 ? avgRating.toFixed(1) : '-'}</span>
                        </div>
                    </div>
                </div>
            </article>
        `;
    }).join('');
}

/**
 * Handle search input
 */
function handleSearch(e) {
    const query = e.target.value.trim();

    // Reset filter to 'all' when searching
    filterBtns.forEach(btn => btn.classList.remove('active'));
    document.querySelector('[data-filter="all"]').classList.add('active');
    currentFilter = 'all';

    if (query === '') {
        renderMovies(getMovies());
    } else {
        renderMovies(searchMovies(query));
    }
}

/**
 * Handle filter button click
 */
function handleFilter(btn) {
    // Clear search
    searchInput.value = '';

    // Update active state
    filterBtns.forEach(b => b.classList.remove('active'));
    btn.classList.add('active');

    currentFilter = btn.dataset.filter;
    renderMovies(filterByGenre(currentFilter));
}

/**
 * Open movie modal
 */
function openMovieModal(movieId) {
    const movie = getMovieById(movieId);
    if (!movie) return;

    const avgRating = getAverageRating(movieId);
    const reviewCount = movie.reviews ? movie.reviews.length : 0;

    modalBody.innerHTML = `
        <div class="movie-detail">
            <div class="movie-detail-poster">
                <img src="${movie.poster}" alt="${movie.title}">
            </div>
            <div class="movie-detail-info">
                <div class="movie-detail-header">
                    <h2 class="movie-detail-title">${movie.title}</h2>
                    <div class="movie-detail-meta">
                        <span>${movie.year}</span>
                        <span class="separator">•</span>
                        <span>${movie.director}</span>
                        <span class="separator">•</span>
                        <span>${movie.genre}</span>
                    </div>
                </div>

                <div class="movie-detail-rating">
                    <div class="stars-display">
                        ${generateStars(avgRating)}
                    </div>
                    <div class="rating-info">
                        <span class="rating-number">${avgRating > 0 ? avgRating.toFixed(1) : 'No ratings'}</span>
                        <span class="rating-count">${reviewCount} review${reviewCount !== 1 ? 's' : ''}</span>
                    </div>
                </div>

                <p class="movie-detail-plot">${movie.plot}</p>

                <div class="review-section">
                    <h3>Write a Review</h3>
                    <form class="review-form" onsubmit="submitReview(event, ${movie.id})">
                        <div class="form-row">
                            <div class="form-group">
                                <label for="reviewerName">Your Name</label>
                                <input type="text" id="reviewerName" required placeholder="Enter your name">
                            </div>
                            <div class="form-group">
                                <label>Your Rating</label>
                                <div class="star-rating">
                                    <input type="radio" id="star5" name="rating" value="5" required>
                                    <label for="star5">★</label>
                                    <input type="radio" id="star4" name="rating" value="4">
                                    <label for="star4">★</label>
                                    <input type="radio" id="star3" name="rating" value="3">
                                    <label for="star3">★</label>
                                    <input type="radio" id="star2" name="rating" value="2">
                                    <label for="star2">★</label>
                                    <input type="radio" id="star1" name="rating" value="1">
                                    <label for="star1">★</label>
                                </div>
                            </div>
                        </div>
                        <div class="form-group full-width">
                            <label for="reviewComment">Your Review</label>
                            <textarea id="reviewComment" required placeholder="What did you think of this movie?"></textarea>
                        </div>
                        <button type="submit" class="submit-btn">Submit Review</button>
                    </form>

                    <div class="reviews-list" id="reviewsList">
                        ${renderReviews(movie.reviews)}
                    </div>
                </div>
            </div>
        </div>
    `;

    movieModal.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
}

/**
 * Close movie modal
 */
function closeMovieModal() {
    movieModal.classList.add('hidden');
    document.body.style.overflow = '';
}

/**
 * Generate star HTML
 */
function generateStars(rating) {
    let stars = '';
    for (let i = 1; i <= 5; i++) {
        stars += `<span class="star ${i <= Math.round(rating) ? 'filled' : ''}">★</span>`;
    }
    return stars;
}

/**
 * Render reviews list
 */
function renderReviews(reviews) {
    if (!reviews || reviews.length === 0) {
        return '<p class="no-reviews">No reviews yet. Be the first to review!</p>';
    }

    return reviews.map(review => `
        <div class="review-card">
            <div class="review-header">
                <span class="reviewer-name">${review.name}</span>
                <span class="review-stars">${'★'.repeat(review.rating)}${'☆'.repeat(5 - review.rating)}</span>
            </div>
            <p class="review-comment">${review.comment}</p>
        </div>
    `).reverse().join('');
}

/**
 * Submit a review
 */
function submitReview(event, movieId) {
    event.preventDefault();

    const name = document.getElementById('reviewerName').value.trim();
    const rating = parseInt(document.querySelector('input[name="rating"]:checked').value);
    const comment = document.getElementById('reviewComment').value.trim();

    if (!name || !rating || !comment) {
        showToast('Please fill in all fields', 'error');
        return;
    }

    // Save the review
    const review = { name, rating, comment };
    saveReview(movieId, review);

    // Refresh the modal content
    openMovieModal(movieId);

    // Refresh the grid to update ratings
    if (searchInput.value.trim()) {
        renderMovies(searchMovies(searchInput.value.trim()));
    } else {
        renderMovies(filterByGenre(currentFilter));
    }

    showToast('Review submitted successfully!');
}

/**
 * Show toast notification
 */
function showToast(message, type = 'success') {
    const toast = document.createElement('div');
    toast.className = `toast ${type}`;
    toast.textContent = message;
    document.body.appendChild(toast);

    setTimeout(() => {
        toast.remove();
    }, 3000);
}

// Initialize the app when DOM is ready
document.addEventListener('DOMContentLoaded', init);
