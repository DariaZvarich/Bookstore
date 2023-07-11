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

def test_get_wave_with_argument(web_client):
    response = web_client.get('/wave?name=Dana')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'I am waving at Dana'
    

"""
When i send a request POST submit
With arguments name = "Dana" and message = 'Hello'
I expect the status code to be 200 OK
And th eresponse to be 'Thanks Dana, you sent this message: "Hello"' 
"""

def test_post_submit_with_arguments(web_client):
    response = web_client.post('/submit', data={
        'name': 'Dana',
        'message': 'Hello'
    })
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Thanks Dana, you sent this message: "Hello"'