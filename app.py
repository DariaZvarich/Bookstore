import os
from lib.database_connection import get_flask_database_connection
from lib.book_repository import BookRepository
from flask import Flask, request
from lib.book import Book

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route('/books')
def get_books1():
    connection = get_flask_database_connection(app)
    repository = BookRepository(connection)
    books = repository.all()
    books_strings = [f"{book}" for book in books]
    return "\n".join(books_strings)

@app.route('/books/<id>')
def get_books2():
    connection = get_flask_database_connection(app)
    repository = BookRepository(connection)
    book = repository.find(id)
    return str(book)

@app.route('/books', methods=['POST'])
def post_books():
    connection = get_flask_database_connection(app)
    repository = BookRepository(connection)
    title = request.form['title']
    author_name = request.form['author_name']
    book = Book(None, title, author_name)
    repository.create(book)
    return "Book added successfully."

@app.route('/books/<id>', methods=['DELETE'])
def delete_books(id):
    connection = get_flask_database_connection(app)
    repository = BookRepository(connection)
    repository.delete(id)
    return 'Book deleted successfully.'
    
# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://localhost:5000/emoji


# @app.route('/greet', methods=['GET'])
# def get_greet():
#     name = request.args['person']
#     return f"Hello {name}!\n"

# @app.route('/greet', methods=['POST'])
# def post_greet():
#     name = request.args['person']
#     return f"Hello {name}!\n"

# @app.route('/submit', methods=['POST'])
# def post_submit():
#     name = request.form['name']
#     massage = request.form['massage']
#     return f'Thanks {name}, you sent this message: "{massage}"'


# @app.route('/wave', methods=['GET'])
# def post_wave():
#     name = request.form['name']
#     return f'I am waving at {name}'


# ---------------
# @app.route('/wave', methods=["GET"])
# def get_wave():
#     name = request.args['name']
#     return f"I am waving at {name}"

# @app.route('/submit', methods=["POST"])
# def post_submit():
#     name = request.form['name']
#     message = request.form['message']
#     return f'Thanks {name}, you sent this message: "{message}"'

# @app.route('/count_vowels', methods=["POST"])
# def post_count_vowels():
#     text = request.form['text']
#     vowel_number = 0
#     for letter in text:
#         if letter in 'aeiou':
#             vowel_number += 1
#     return f'There are {vowel_number} vowels in "{text}"'

# @app.route('/sort-names', methods=['POST'])
# def post_sort_names():
#     if 'names' not in request.form:
#         return "You didn`t submit any names!", 400
#     names = request.form['names'].split(',')
#     # sorted_names = sorted(names)
#     return ','.join(names)


# @app.route('/names', methods=['GET'])
# def get_sort_names():
#     names = ["Julia", "Alice", "Karim"]
#     to_add = request.args.get('add')
#     if not to_add:
#         return "Error: there is no name added", 400
#     split_names = to_add.split(',')
#     names = names + split_names
#     sorted_names = sorted(names)
#     sorted_names_str = ', '.join(sorted_names)
#     return sorted_names_str
    
    
# @app.route('/books', methods=['GET'])
# def get_books():
#     return ''
    

    
# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

