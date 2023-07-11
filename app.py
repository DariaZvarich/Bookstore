import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

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

@app.route('/count_vowels', methods=["POST"])
def post_count_vowels():
    text = request.form['text']
    vowel_number = 0
    for letter in text:
        if letter in 'aeiou':
            vowel_number += 1
    return f'There are {vowel_number} vowels in "{text}"'


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

