/**
 * Movie Database
 * This file contains all movie data and handles localStorage for reviews
 *
 * YOUR CHALLENGES ARE IN THIS FILE!
 * Look for the TODO comments and complete each challenge.
 */

const moviesData = [
    {
        id: 1,
        title: "The Shawshank Redemption",
        year: 1994,
        genre: "Drama",
        director: "Frank Darabont",
        plot: "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency. A tale of hope and perseverance that has touched millions of hearts worldwide.",
        poster: "https://m.media-amazon.com/images/M/MV5BMDAyY2FhYjctNDc5OS00MDNlLThiMGUtY2UxYWVkNGY2ZjljXkEyXkFqcGc@._V1_SX300.jpg",
        reviews: []
    },
    {
        id: 2,
        title: "The Godfather",
        year: 1972,
        genre: "Crime, Drama",
        director: "Francis Ford Coppola",
        plot: "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant youngest son. An offer you can't refuse.",
        poster: "https://m.media-amazon.com/images/M/MV5BYTJkNGQyZDgtZDQ0NC00MDM0LWEzZWQtYzUzZDEwMDljZWNjXkEyXkFqcGc@._V1_SX300.jpg",
        reviews: []
    },
    {
        id: 3,
        title: "The Dark Knight",
        year: 2008,
        genre: "Action, Crime, Drama",
        director: "Christopher Nolan",
        plot: "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.",
        poster: "https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SX300.jpg",
        reviews: []
    },
    {
        id: 4,
        title: "Pulp Fiction",
        year: 1994,
        genre: "Crime, Drama",
        director: "Quentin Tarantino",
        plot: "The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
        poster: "https://m.media-amazon.com/images/M/MV5BYTViYTE3ZGQtNDBlMC00ZTAyLTkyODMtZGRiZDg0MjA2YThkXkEyXkFqcGc@._V1_SX300.jpg",
        reviews: []
    },
    {
        id: 5,
        title: "Forrest Gump",
        year: 1994,
        genre: "Drama, Romance",
        director: "Robert Zemeckis",
        plot: "The presidencies of Kennedy and Johnson, the Vietnam War, the Watergate scandal and other historical events unfold from the perspective of an Alabama man with an IQ of 75.",
        poster: "https://m.media-amazon.com/images/M/MV5BNDYwNzVjMTItZmU5YS00YjQ5LTljYjgtMjY2NDVmYWMyNWFmXkEyXkFqcGc@._V1_SX300.jpg",
        reviews: []
    },
    {
        id: 6,
        title: "Inception",
        year: 2010,
        genre: "Action, Sci-Fi",
        director: "Christopher Nolan",
        plot: "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.",
        poster: "https://m.media-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SX300.jpg",
        reviews: []
    },
    {
        id: 7,
        title: "The Matrix",
        year: 1999,
        genre: "Action, Sci-Fi",
        director: "Lana Wachowski, Lilly Wachowski",
        plot: "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
        poster: "https://m.media-amazon.com/images/M/MV5BN2NmN2VhMTQtMDNiOS00NDlhLTliMjgtODE2ZTY0ODQyNDRhXkEyXkFqcGc@._V1_SX300.jpg",
        reviews: []
    },
    {
        id: 8,
        title: "Interstellar",
        year: 2014,
        genre: "Adventure, Drama, Sci-Fi",
        director: "Christopher Nolan",
        plot: "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
        poster: "https://m.media-amazon.com/images/M/MV5BYzdjMDAxZGItMjI2My00ODA1LTlkNzItOWFjMDU5ZDJlYWY3XkEyXkFqcGc@._V1_SX300.jpg",
        reviews: []
    },
    {
        id: 9,
        title: "Parasite",
        year: 2019,
        genre: "Drama, Thriller",
        director: "Bong Joon Ho",
        plot: "Greed and class discrimination threaten the newly formed symbiotic relationship between the wealthy Park family and the destitute Kim clan.",
        poster: "https://m.media-amazon.com/images/M/MV5BYjk1Y2U4MjQtY2ZiNS00OWQyLWI3MmYtZWUwNmRjYWRiNWNhXkEyXkFqcGc@._V1_SX300.jpg",
        reviews: []
    },
    {
        id: 10,
        title: "The Lion King",
        year: 1994,
        genre: "Animation, Adventure, Drama",
        director: "Roger Allers, Rob Minkoff",
        plot: "Lion prince Simba and his father are targeted by his bitter uncle, who wants to ascend the throne himself.",
        poster: "https://m.media-amazon.com/images/M/MV5BYTYxNGMyZTYtMjE3MS00MzNjLWFjNmYtMDk3N2FmM2JiM2M1XkEyXkFqcGc@._V1_SX300.jpg",
        reviews: []
    },
    {
        id: 11,
        title: "Gladiator",
        year: 2000,
        genre: "Action, Adventure, Drama",
        director: "Ridley Scott",
        plot: "A former Roman General sets out to exact vengeance against the corrupt emperor who murdered his family and sent him into slavery.",
        poster: "https://m.media-amazon.com/images/M/MV5BYWQ4YmNjYjEtOWE1Zi00Y2U4LWI4NTAtMTU0MjkxNWQ1ZmJiXkEyXkFqcGc@._V1_SX300.jpg",
        reviews: []
    },
    {
        id: 12,
        title: "Titanic",
        year: 1997,
        genre: "Drama, Romance",
        director: "James Cameron",
        plot: "A seventeen-year-old aristocrat falls in love with a kind but poor artist aboard the luxurious, ill-fated R.M.S. Titanic.",
        poster: "https://m.media-amazon.com/images/M/MV5BYzYyN2FiZmUtYWYzMy00MzViLWJkZTMtOGY1ZjgzNWMzZTEwXkEyXkFqcGc@._V1_SX300.jpg",
        reviews: []
    },
    {
        id: 13,
        title: "Avatar",
        year: 2009,
        genre: "Action, Adventure, Sci-Fi",
        director: "James Cameron",
        plot: "A paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
        poster: "https://m.media-amazon.com/images/M/MV5BMDEzMmQwZjctZWU2My00MWNlLWE0NjItMDJlYTRlNGJiZjcyXkEyXkFqcGc@._V1_SX300.jpg",
        reviews: []
    },
    {
        id: 14,
        title: "Jurassic Park",
        year: 1993,
        genre: "Action, Adventure, Sci-Fi",
        director: "Steven Spielberg",
        plot: "A pragmatic paleontologist touring an almost complete theme park on an island is tasked with protecting a couple of kids after a power failure causes the park's cloned dinosaurs to run loose.",
        poster: "https://m.media-amazon.com/images/M/MV5BMjM2MDgxMDg0Nl5BMl5BanBnXkFtZTgwNTM2OTM5NDE@._V1_SX300.jpg",
        reviews: []
    },
    {
        id: 15,
        title: "The Avengers",
        year: 2012,
        genre: "Action, Sci-Fi",
        director: "Joss Whedon",
        plot: "Earth's mightiest heroes must come together and learn to fight as a team if they are going to stop the mischievous Loki and his alien army from enslaving humanity.",
        poster: "https://m.media-amazon.com/images/M/MV5BNGE0YTVjNzUtNzJjOS00NGNlLTgxMzctZTY4YTE1Y2Y1ZTU4XkEyXkFqcGc@._V1_SX300.jpg",
        reviews: []
    },
    {
        id: 16,
        title: "Black Panther",
        year: 2018,
        genre: "Action, Adventure, Sci-Fi",
        director: "Ryan Coogler",
        plot: "T'Challa, heir to the hidden but advanced kingdom of Wakanda, must step forward to lead his people into a new future and must confront a challenger from his country's past.",
        poster: "https://m.media-amazon.com/images/M/MV5BNTM4NjIxNmEtYWE5NS00NDczLTkyNWQtYThhNmQyZGQzMjM0XkEyXkFqcGc@._V1_SX300.jpg",
        reviews: []
    },
    {
        id: 17,
        title: "Spirited Away",
        year: 2001,
        genre: "Animation, Adventure, Family",
        director: "Hayao Miyazaki",
        plot: "During her family's move to the suburbs, a sullen 10-year-old girl wanders into a world ruled by gods, witches and spirits, a world where humans are changed into beasts.",
        poster: "https://m.media-amazon.com/images/M/MV5BNTEyNmEwOWUtYzkyOC00ZTQ4LTllZmUtMjk0Y2YwOGUzYjRiXkEyXkFqcGc@._V1_SX300.jpg",
        reviews: []
    },
    {
        id: 18,
        title: "Get Out",
        year: 2017,
        genre: "Horror, Mystery, Thriller",
        director: "Jordan Peele",
        plot: "A young African-American visits his white girlfriend's parents for the weekend, where his simmering uneasiness about their reception of him eventually reaches a boiling point.",
        poster: "https://m.media-amazon.com/images/M/MV5BMjUxMDQwNjcyNl5BMl5BanBnXkFtZTgwNzcwMzc0MTI@._V1_SX300.jpg",
        reviews: []
    },
    {
        id: 19,
        title: "Coco",
        year: 2017,
        genre: "Animation, Adventure, Drama",
        director: "Lee Unkrich, Adrian Molina",
        plot: "Aspiring musician Miguel, confronted with his family's ancestral ban on music, enters the Land of the Dead to find his great-great-grandfather, a legendary singer.",
        poster: "https://m.media-amazon.com/images/M/MV5BYjQ5NjM0Y2YtNjZkNC00ZDhkLWJjMWItN2QyNzFkMDE3ZjAxXkEyXkFqcGc@._V1_SX300.jpg",
        reviews: []
    },
    {
        id: 20,
        title: "Spider-Man: Into the Spider-Verse",
        year: 2018,
        genre: "Animation, Action, Adventure",
        director: "Bob Persichetti, Peter Ramsey",
        plot: "Teen Miles Morales becomes the Spider-Man of his universe and must join with five spider-powered individuals from other dimensions to stop a threat for all realities.",
        poster: "https://m.media-amazon.com/images/M/MV5BMjMwNDkxMTgzOF5BMl5BanBnXkFtZTgwNTkwNTQ3NjM@._V1_SX300.jpg",
        reviews: []
    }
];


// ============================================================
// CHALLENGE 1: Get All Movies
// ============================================================
/**
 * Get all movies with their reviews from localStorage
 *
 * This function should:
 * 1. Check if there are saved reviews in localStorage
 * 2. If yes, merge them with the movie data
 * 3. Return all movies
 */
function getMovies() {
    // Check if we have reviews saved in localStorage
    const savedReviews = localStorage.getItem('movieReviews');

    if (savedReviews) {
        const reviewsMap = JSON.parse(savedReviews);
        // Merge saved reviews with movie data
        return moviesData.map(movie => ({
            ...movie,
            reviews: reviewsMap[movie.id] || []
        }));
    }

    return moviesData;
}


// ============================================================
// CHALLENGE 2: Find a Movie by ID
// ============================================================
/**
 * Get a single movie by its ID
 *
 * TODO: Complete this function!
 *
 * Steps:
 * 1. Get all movies using getMovies()
 * 2. Find the movie where movie.id equals the id parameter
 * 3. Return that movie
 *
 * HINT: Use the .find() method on arrays
 * Example: array.find(item => item.id === id)
 */
function getMovieById(id) {
    // TODO: Get all movies
    // TODO: Find and return the movie with matching id

    return null; // Replace this!
}


// ============================================================
// CHALLENGE 3: Save a Review
// ============================================================
/**
 * Save a review for a movie
 *
 * TODO: Complete this function!
 *
 * The review object looks like: { name: "John", rating: 5, comment: "Great!" }
 *
 * Steps:
 * 1. Get existing reviews from localStorage (key: 'movieReviews')
 * 2. Parse it as JSON, or create empty object if none exists
 * 3. If this movie doesn't have a reviews array yet, create one
 * 4. Push the new review to the movie's reviews array
 * 5. Save back to localStorage
 *
 * HINTS:
 * - localStorage.getItem('movieReviews') gets saved data
 * - JSON.parse() converts string to object
 * - JSON.stringify() converts object to string
 * - localStorage.setItem('movieReviews', data) saves data
 */
function saveReview(movieId, review) {
    // TODO: Get existing reviews from localStorage
    // const savedReviews = localStorage.getItem('movieReviews');

    // TODO: Parse it or create empty object
    // const reviewsMap = savedReviews ? JSON.parse(savedReviews) : {};

    // TODO: Initialize array for this movie if it doesn't exist
    // if (!reviewsMap[movieId]) {
    //     reviewsMap[movieId] = [];
    // }

    // TODO: Add the new review

    // TODO: Save back to localStorage
}


// ============================================================
// CHALLENGE 4: Calculate Average Rating
// ============================================================
/**
 * Calculate the average rating for a movie
 *
 * TODO: Complete this function!
 *
 * Steps:
 * 1. Get the movie by ID
 * 2. If no movie found or no reviews, return 0
 * 3. Add up all the ratings
 * 4. Divide by the number of reviews
 * 5. Return the average
 *
 * HINTS:
 * - Use getMovieById() to get the movie
 * - movie.reviews is an array of review objects
 * - Each review has a .rating property
 * - You can use a for loop or .reduce() to sum values
 */
function getAverageRating(movieId) {
    // TODO: Get the movie

    // TODO: Check if movie exists and has reviews

    // TODO: Calculate the total of all ratings

    // TODO: Return the average (total / number of reviews)

    return 0; // Replace this!
}


// ============================================================
// CHALLENGE 5: Search Movies
// ============================================================
/**
 * Search movies by title
 *
 * TODO: Complete this function!
 *
 * Steps:
 * 1. Get all movies
 * 2. Convert the search query to lowercase
 * 3. Filter movies where the title contains the query
 * 4. Return the filtered list
 *
 * HINTS:
 * - Use .toLowerCase() to make search case-insensitive
 * - Use .filter() to get matching movies
 * - Use .includes() to check if title contains query
 *
 * Example: "dark".includes("ark") returns true
 */
function searchMovies(query) {
    // TODO: Get all movies

    // TODO: Convert query to lowercase

    // TODO: Filter and return movies where title includes query

    return []; // Replace this!
}


// ============================================================
// CHALLENGE 6: Filter by Genre (BONUS)
// ============================================================
/**
 * Filter movies by genre
 *
 * TODO: Complete this function!
 *
 * Steps:
 * 1. Get all movies
 * 2. If genre is 'all', return all movies
 * 3. If genre is 'top-rated', return movies with average rating >= 4
 * 4. Otherwise, filter movies that include the genre
 *
 * HINTS:
 * - movie.genre is a string like "Action, Sci-Fi"
 * - Use .includes() to check if genre is in the string
 * - Use getAverageRating() for top-rated filter
 */
function filterByGenre(genre) {
    const movies = getMovies();

    if (genre === 'all') {
        return movies;
    }

    if (genre === 'top-rated') {
        // TODO: Return movies where average rating is 4 or higher
        return movies; // Replace this!
    }

    // TODO: Return movies that include this genre
    return movies; // Replace this!
}
