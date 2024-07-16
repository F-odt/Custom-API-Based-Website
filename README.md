## Custom API Based Website
### Overview

This project is a Flask-based web application that explores data from the world of Middle-earth using the public API The One API. The application provides comprehensive information about characters, books, and movies from The Lord of the Rings universe. The data is fetched using HTTP requests and REST APIs, and displayed in a tile layout with pagination for large datasets.
Features

    Fetch and display information about characters, books, and movies from The One API.
    Paginated list views for characters.
    Detail views for books, movies, and characters with additional information.
    Hyperlinks to more detailed information.
    Responsive tile layout for data presentation.
    Built using HTML, JavaScript, CSS, and Flask.

### Prerequisites

    Python 3.x
    Flask
    Requests library

### Configuration
    API Key: Obtain an API key from The One API by signing up.
    Config: Create a configuration file named config.py in the root directory of your project with the following content:
    class Config:
        API_KEY = 'your_api_key_here'

### Installation
     1. Clone The Repository:
        git clone https://github.com/F-odt/Custom-API-Based-Website.git

### Create a virtual environment:
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

### Install dependencies:
    pip install -r requirements.txt

### Create the configuration file:
    echo "class Config:\n    API_KEY = 'your_api_key_here'" > config.py

## Running The Application
### 1. Start the Flask application:
        python app.py

### 2. Open your web browser 
    and navigate to http://127.0.0.1:5000 to view the application.

## Application Structure
    app.py: The main Flask application file.
templates/: Directory containing HTML templates.

    home.html: Template for the home page.
    books.html: Template for displaying books.
    book_detail.html: Template for displaying book details and chapters.
    movies.html: Template for displaying movies.
    movie_detail.html: Template for displaying movie details and quotes.
    characters.html: Template for displaying characters with pagination.
    character_detail.html: Template for displaying character details and quotes.
    quotes.html: Template for displaying quotes.
    chapters.html: Template for displaying chapters.

static/: Directory containing static files (CSS, JavaScript).

    css/style.css: Stylesheet for the application.
    js/script.js: JavaScript file for the application.
