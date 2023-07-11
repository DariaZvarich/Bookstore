{{ NAME }} Route Design Recipe
Copy this design recipe template to test-drive a plain-text Flask route.

# Request:
POST http://localhost:5000/sort-names

# With body parameters:
names=Joe,Alice,Zoe,Julia,Kieran

# Expected response (sorted list of names):
Alice,Joe,Julia,Kieran,Zoe

1. Design the Route Signature
Include the HTTP method, the path, and any query or body parameters.

# EXAMPLE

POST /sort.names
    names: a string of comma separated names (no spaces)


2. Create Examples as Tests
Go through each route and write down one or more example responses.

Remember to try out different parameter values.

Include the status code and the response body.

    python
# POST /sort-names
# With names=Joe,Alice,Zoe,Julia,Kieran
# Expected response (200 OK)
"""
Alice, Joe, Julia, Kieran, Zoe
"""

# POST /sort-names
# With names=Aaaaa,Aaaaz,Aaaab
# Expected response (200 OK)
"""
Aaaaa, Aaaaz, Aaaab
"""

# POST /sort-names
# With no names
# Expected response Invalid Request code
"""
You didn`t submit any names!
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
