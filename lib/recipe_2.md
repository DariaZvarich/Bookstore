{{ NAME }} Route Design Recipe
Copy this design recipe template to test-drive a plain-text Flask route.

# Request:
GET /names?add=Eddie

# This route should return a list of pre-defined names, plus the name given.

# Expected response (2OO OK):
Julia, Alice, Karim, Eddie

1. Design the Route Signature
Include the HTTP method, the path, and any query or body parameters.

# EXAMPLE

GET /names.add
    names: a string of comma separeted names(no spaces)


2. Create Examples as Tests
Go through each route and write down one or more example responses.

Remember to try out different parameter values.

Include the status code and the response body.

# EXAMPLE


    python
# GET /names-add
# With names = Julia, Alice, Karim, Eddie
# Expected response (200 OK)

"""
Alice, Eddie, Julia, Karim
"""

# GET /names-add
# With names = Julia, Alice, Karim
# Expected response (400 OK)

"""
Error: there is no name added
"""

# GET /names-add
# With names = Julia, Alice, Karim
# Expected response (400 OK)

"""
Error: zero parameters
"""

# GET /names-add
# With names = Julia, Alice, Karim
# Expected response (200 OK)

"""
Alice, Eddie, Julia, Karim, Leo

"""









# GET /home
#  Expected response (200 OK):
"""
This is my home page!
"""

# GET /wave?name=Leo
#  Expected response (200 OK):
"""
I am waving at Leo
"""

# GET /wave
#  Expected response (200 OK):
"""
I am waving at no one!
"""

# POST /submit
#  Parameters:
#    name: Leo
#    message: Hello world
#  Expected response (200 OK):
"""
Thanks Leo, you sent this message: "Hello world"
"""

# POST /submit
#  Parameters: none
#  Expected response (400 Bad Request):
"""
Please provide a name and a message
"""
3. Test-drive the Route
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

Here's an example for you to start with:

"""
GET /home
  Expected response (200 OK):
  "This is my home page!"
"""
def test_get_home(web_client):
    response = web_client.get('/home')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'This is my home page!'

"""
POST /submit
  Parameters:
    name: Leo
    message: Hello world
  Expected response (200 OK):
  "Thanks Leo, you sent this message: "Hello world""
"""
def test_post_submit(web_client):
    response = web_client.post('/submit', data={'name': 'Leo', 'message': 'Hello world'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Thanks Leo, you sent this message: "Hello world"'
