# Tests for your routes go here

# === Example Code Below ===

"""
GET /emoji
"""
"""
When i send a request GET /wave?name=Dana
I expect the status code to be 200 OK
And the response to be 'I am waving at Dana'
"""

# === End Example Code ===

# def test_get_wave_with_argument(web_client):
#     response = web_client.get('/wave?name=Dana')
#     assert response.status_code == 200
#     assert response.data.decode('utf-8') == 'I am waving at Dana'
    

# """
# When i send a request POST submit
# With arguments name = "Dana" and message = 'Hello'
# I expect the status code to be 200 OK
# And th eresponse to be 'Thanks Dana, you sent this message: "Hello"' 
# """

# def test_post_submit_with_arguments(web_client):
#     response = web_client.post('/submit', data={
#         'name': 'Dana',
#         'message': 'Hello'
#     })
#     assert response.status_code == 200
#     assert response.data.decode('utf-8') == 'Thanks Dana, you sent this message: "Hello"'
    
#     """
# When: I make a POST request to /count_vowels
# And: I send "eee" as the body parameter text
# Then: I should get a 200 response with 3 in the message
"""
def test_post_count_vowels_eee(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eee'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 3 vowels in "eee"'

"""
"""
When: I make a POST request to /count_vowels
And: I send "eunoia" as the body parameter text
Then: I should get a 200 response with 5 in the message
"""
# def test_post_count_vowels_eunoia(web_client):
#     response = web_client.post('/count_vowels', data={'text': 'eunoia'})
#     assert response.status_code == 200
#     assert response.data.decode('utf-8') == 'There are 5 vowels in "eunoia"'

# """
# When: I make a POST request to /count_vowels
# And: I send "mercurial" as the body parameter text
# Then: I should get a 200 response with 4 in the message
# """
# def test_post_count_vowels_mercurial(web_client):
#     response = web_client.post('/count_vowels', data={'text': 'mercurial'})
#     assert response.status_code == 200
#     assert response.data.decode('utf-8') == 'There are 4 vowels in "mercurial"'


# POST /sort-names
# With names=Joe,Alice,Zoe,Julia,Kieran
# Expected response (200 OK)
"""
Alice, Joe, Julia, Kieran, Zoe
"""
# def test_post_sort_names_with_a_list_of_names(web_client):
#     response = web_client.post("/sort-names", data={
#         'names': 'Alice, Joe, Julia, Kieran, Zoe'
#     })
#     assert response.status_code == 200
#     assert response.data.decode('utf-8') == 'Alice, Joe, Julia, Kieran, Zoe'

# # POST /sort-names
# # With names=Aaaaa,Aaaaz,Aaaab
# # Expected response (200 OK)
# """
# Aaaaa, Aaaaz, Aaaab
# """

# def test_post_sort_names_with_a_list_of_names_with_letters_at_the_end(web_client):
#     response = web_client.post("/sort-names", data={
#         'names': 'Aaaaa, Aaaaz, Aaaab'
#     })
#     assert response.status_code == 200
#     assert response.data.decode('utf-8') == 'Aaaaa, Aaaaz, Aaaab'


# # POST /sort-names
# # With no names
# # Expected response Invalid Request code
# """
# You didn`t submit any names!
# """

# def test_post_sort_names_with_no_list_of_names(web_client):
#     response = web_client.post("/sort-names")
#     assert response.status_code == 400
#     assert response.data.decode('utf-8') == 'You didn`t submit any names!'


"""
When i missed to add the parameter
I get error 400  
"""

# def test_400_when_no_parameter(web_client):
#     response = web_client.get("/names")
#     assert response.status_code == 400

"""
When i add empty string
I get error 400  
"""

# def test_get_empty_string(web_client):
#     response = web_client.get("/names?=")
#     assert response.status_code == 400


"""
When i add the name
I get the list of names with added name and 200 OK
"""

# def test_get_add_name(web_client):
#     response = web_client.get("/names?add=Eddie")
#     assert response.status_code == 200
#     assert response.data.decode('utf-8') == 'Alice, Eddie, Julia, Karim'


# """
# When i add multiple names
# I get the list of names with added names and 200 OK
# """

# def test_get_add_multiples_names(web_client):
#     response = web_client.get("/names?add=Eddie,Leo")
#     assert response.status_code == 200
#     assert response.data.decode('utf-8') == 'Alice, Eddie, Julia, Karim, Leo'


"""
GET /books
Returns a list of books
"""

def test_get_books(web_client, db_connection):
    db_connection.seed('seeds/book_store.sql')
    response = web_client.get('/books')
    assert response.status_code == 200
    assert response.data.decode('utf-8') ==  \
        "Book(1, Invisible Cities, Italo Calvino)\n" \
        "Book(2, The Man Who Was Thursday, GK Chesterton)\n" \
        "Book(3, Bluets, Maggie Nelson)\n" \
        "Book(4, No Place on Earth, Christa Wolf)\n" \
        "Book(5, Nevada, Imogen Binnie)"
        
        
"""
GET /books/<id>
Returns a single book
"""

def test_get_book2(web_client, db_connection):
    db_connection.seed('seeds/book_store.sql')
    response = web_client.get('/books')
    assert response.status_code == 200
    
    expected_book = "Book(1, Invisible Cities, Italo Calvino)"
    assert expected_book in response.data.decode('utf-8')
"""
POST /books
Creates a book based on the parameters
"""
def test_post_books(web_client, db_connection):
    db_connection.seed('seeds/book_store.sql')
    response = web_client.post('/books', data={
        'title': 'Out of the Crisis', 
        'author_name': 'W Edwards Deming'
    })
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Book added successfully."
    
    response = web_client.get('/books')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "" \
        "Book(1, Invisible Cities, Italo Calvino)\n" \
        "Book(2, The Man Who Was Thursday, GK Chesterton)\n" \
        "Book(3, Bluets, Maggie Nelson)\n" \
        "Book(4, No Place on Earth, Christa Wolf)\n" \
        "Book(5, Nevada, Imogen Binnie)\n" \
        "Book(6, Out of the Crisis, W Edwards Deming)"
"""
DELETE /books/<id>
Deletes thes specified book
"""
def test_delete_book(web_client, db_connection):
    db_connection.seed('seeds/book_store.sql')
    response = web_client.delete('/books/2')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Book deleted successfully"
    
    response = web_client.get('/books')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == (
        "Book(1, Invisible Cities, Italo Calvino)\n"
        "Book(3, Bluets, Maggie Nelson)\n" 
        "Book(4, No Place on Earth, Christa Wolf)\n"
        "Book(5, Nevada, Imogen Binnie)"
    )