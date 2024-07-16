from flask import Flask, render_template, request, jsonify
import requests
from config import Config

# Initialize the Flask application
app = Flask(__name__)
app.config.from_object(Config)

# Define the base URL for the API and the API key from the configuration
API_BASE_URL = "https://the-one-api.dev/v2"
API_KEY = app.config['API_KEY']


# Function to fetch data from the API
def get_data(endpoint, params=None):
    # Set the authorization headers for endpoints other than '/book'
    headers = {"Authorization": f"Bearer {API_KEY}"} if endpoint != "/book" else {}
    try:
        # Make the GET request to the API
        response = requests.get(f"{API_BASE_URL}{endpoint}", headers=headers, params=params)
        # Raise an exception for HTTP errors
        response.raise_for_status()
        # Return the JSON response
        return response.json()
    except requests.RequestException as e:
        # Log any errors that occur during the request
        app.logger.error(f"Error fetching data from {endpoint}: {str(e)}")
        return None


# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')


# Route for the books page
@app.route('/books')
def books():
    data = get_data("/book")
    if data:
        books = data['docs']
        return render_template('books.html', books=books)
    return "Error fetching books", 500


# Route for the book detail page
@app.route('/book/<string:id>')
def book_detail(id):
    book_data = get_data(f"/book/{id}")
    chapters_data = get_data(f"/book/{id}/chapter")

    if book_data and 'docs' in book_data and book_data['docs']:
        book = book_data['docs'][0]
        chapters = chapters_data['docs'] if chapters_data and 'docs' in chapters_data else None
        return render_template('book_detail.html', book=book, chapters=chapters)
    return "Error fetching book details", 500


# Route for the movies page
@app.route('/movies')
def movies():
    try:
        data = get_data("/movie")
        if data:
            movies = data['docs']
            return render_template('movies.html', movies=movies)
        else:
            app.logger.error("No data returned from get_data for /movie")
    except Exception as e:
        app.logger.error(f"Exception in movies route: {str(e)}")
    return "Error fetching movies", 500


# Route for the movie detail page
@app.route('/movie/<string:id>')
def movie_detail(id):
    data = get_data(f"/movie/{id}")
    if data:
        movie = data['docs'][0]
        quotes = get_data(f"/movie/{id}/quote")
        return render_template('movie_detail.html', movie=movie, quotes=quotes['docs'] if quotes else None)
    return "Error fetching movie details", 500


# Route for the characters page
@app.route('/characters')
def characters():
    page = request.args.get('page', 1, type=int)
    limit = 20  # Number of items per page
    data = get_data("/character", params={"limit": limit, "page": page})
    if data:
        characters = data['docs']
        total_pages = data['pages']
        return render_template('characters.html', characters=characters, page=page, total_pages=total_pages)
    return "Error fetching characters", 500


# Route for the character detail page
@app.route('/character/<string:id>')
def character_detail(id):
    data = get_data(f"/character/{id}")
    if data:
        character = data['docs'][0]
        quotes = get_data(f"/character/{id}/quote")
        return render_template('character_detail.html', character=character, quotes=quotes['docs'] if quotes else None)
    return "Error fetching character details", 500


# Route for the quotes page
@app.route('/quotes')
def quotes():
    data = get_data("/quote")
    if data:
        quotes = data['docs']
        return render_template('quotes.html', quotes=quotes)
    return "Error fetching quotes", 500


# Route for the chapters page
@app.route('/chapters')
def chapters():
    data = get_data("/chapter")
    if data:
        chapters = data['docs']
        return render_template('chapters.html', chapters=chapters)
    return "Error fetching chapters", 500


# Run the Flask application in debug mode
if __name__ == '__main__':
    app.run(debug=True)
