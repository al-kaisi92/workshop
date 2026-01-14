/**
 * Movie Database
 * This file contains all movie data and handles localStorage for reviews
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

/**
 * Get all movies with their reviews from localStorage
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

/**
 * Get a single movie by ID
 */
function getMovieById(id) {
    const movies = getMovies();
    return movies.find(movie => movie.id === id);
}

/**
 * Save a review for a movie
 */
function saveReview(movieId, review) {
    // Get existing reviews from localStorage
    const savedReviews = localStorage.getItem('movieReviews');
    const reviewsMap = savedReviews ? JSON.parse(savedReviews) : {};

    // Initialize array for this movie if it doesn't exist
    if (!reviewsMap[movieId]) {
        reviewsMap[movieId] = [];
    }

    // Add the new review
    reviewsMap[movieId].push(review);

    // Save back to localStorage
    localStorage.setItem('movieReviews', JSON.stringify(reviewsMap));
}

/**
 * Calculate average rating for a movie
 */
function getAverageRating(movieId) {
    const movie = getMovieById(movieId);
    if (!movie || !movie.reviews || movie.reviews.length === 0) {
        return 0;
    }

    const total = movie.reviews.reduce((sum, review) => sum + review.rating, 0);
    return total / movie.reviews.length;
}

/**
 * Search movies by title
 */
function searchMovies(query) {
    const movies = getMovies();
    const lowerQuery = query.toLowerCase();
    return movies.filter(movie =>
        movie.title.toLowerCase().includes(lowerQuery)
    );
}

/**
 * Filter movies by genre
 */
function filterByGenre(genre) {
    const movies = getMovies();
    if (genre === 'all') {
        return movies;
    }
    if (genre === 'top-rated') {
        return movies.filter(movie => getAverageRating(movie.id) >= 4);
    }
    return movies.filter(movie =>
        movie.genre.toLowerCase().includes(genre.toLowerCase())
    );
}
