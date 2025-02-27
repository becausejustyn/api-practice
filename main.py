import json
import requests

# Base URL for examples
BASE_URL = "https://jsonplaceholder.typicode.com"
URL = 'https://pokeapi.co/api/v2/pokemon/'

# https://pokeapi.co/docs/v2#pokemon

def pokemon(pokemon: str):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
    if response.status_code == 200:
        pokemon_data = response.json()
        print(f"Name: {pokemon_data['name']}")
        print(f"Height: {pokemon_data['height']}")
        print(f"Weight: {pokemon_data['weight']}")
        print(f"Types: {', '.join([t['type']['name'] for t in pokemon_data['types']])}")
    else:
        print(f"Error fetching data: {response.status_code}")


# ----------------------
# GET Request Example
# ----------------------
def get_example():
    """Fetch a resource with a GET request"""
    print("\n=== GET Request Example ===")
    
    # Make the GET request
    response = requests.get(f"{BASE_URL}/posts/1")
    
    # Check if request was successful
    if response.status_code == 200:
        data = response.json()
        print(f"Status Code: {response.status_code}")
        print(f"Title: {data['title']}")
        print(f"Body: {data['body']}")
    else:
        print(f"Failed with status code: {response.status_code}")
    
    # You can also include query parameters
    params = {"userId": 1}
    response = requests.get(f"{BASE_URL}/posts", params=params)
    print(f"\nGET with query params - Status Code: {response.status_code}")
    print(f"Number of posts returned: {len(response.json())}")

# ----------------------
# POST Request Example
# ----------------------
def post_example():
    """Create a resource with a POST request"""
    print("\n=== POST Request Example ===")
    
    # Data to send in the request body
    new_post = {
        "title": "My New Post",
        "body": "This is the content of my new post.",
        "userId": 1
    }
    
    # Make the POST request
    response = requests.post(f"{BASE_URL}/posts", json=new_post)
    
    # Check if request was successful
    if response.status_code == 201:  # 201 Created
        data = response.json()
        print(f"Status Code: {response.status_code}")
        print(f"Created post with ID: {data['id']}")
        print(f"Title: {data['title']}")
    else:
        print(f"Failed with status code: {response.status_code}")
    
    # Alternative: Using data parameter instead of json
    headers = {"Content-Type": "application/json"}
    response = requests.post(
        f"{BASE_URL}/posts", 
        data=json.dumps(new_post),
        headers=headers
    )
    print(f"\nPOST with headers - Status Code: {response.status_code}")

# ----------------------
# PUT Request Example
# ----------------------
def put_example():
    """Update a resource with a PUT request"""
    print("\n=== PUT Request Example ===")
    
    # Data for complete resource replacement
    updated_post = {
        "id": 1,
        "title": "Updated Title",
        "body": "This post has been completely updated.",
        "userId": 1
    }
    
    # Make the PUT request
    response = requests.put(f"{BASE_URL}/posts/1", json=updated_post)
    
    # Check if request was successful
    if response.status_code == 200:
        data = response.json()
        print(f"Status Code: {response.status_code}")
        print(f"Updated title: {data['title']}")
    else:
        print(f"Failed with status code: {response.status_code}")

# ----------------------
# PATCH Request Example
# ----------------------
def patch_example():
    """Partially update a resource with a PATCH request"""
    print("\n=== PATCH Request Example ===")
    
    # Only updating the title
    patch_data = {
        "title": "Patched Title"
    }
    
    # Make the PATCH request
    response = requests.patch(f"{BASE_URL}/posts/1", json=patch_data)
    
    # Check if request was successful
    if response.status_code == 200:
        data = response.json()
        print(f"Status Code: {response.status_code}")
        print(f"Patched title: {data['title']}")
        print(f"Body remains: {data['body']}")
    else:
        print(f"Failed with status code: {response.status_code}")

# ----------------------
# DELETE Request Example
# ----------------------
def delete_example():
    """Delete a resource with a DELETE request"""
    print("\n=== DELETE Request Example ===")
    
    # Make the DELETE request
    response = requests.delete(f"{BASE_URL}/posts/1")
    
    # Check if request was successful
    if response.status_code == 200 or response.status_code == 204:
        print(f"Status Code: {response.status_code}")
        print("Resource successfully deleted")
    else:
        print(f"Failed with status code: {response.status_code}")

# ----------------------
# HEAD Request Example
# ----------------------
def head_example():
    """Get only headers with a HEAD request"""
    print("\n=== HEAD Request Example ===")
    
    # Make the HEAD request
    response = requests.head(f"{BASE_URL}/posts/1")
    
    # Print headers
    print(f"Status Code: {response.status_code}")
    print("Headers:")
    for key, value in response.headers.items():
        print(f"  {key}: {value}")
    
    # Note: HEAD requests don't return a body
    print(f"Body length: {len(response.text)}")  # Will be 0

# ----------------------
# OPTIONS Request Example
# ----------------------
def options_example():
    """Get allowed methods with an OPTIONS request"""
    print("\n=== OPTIONS Request Example ===")
    
    # Make the OPTIONS request
    response = requests.options(f"{BASE_URL}")
    
    # Print allowed methods
    print(f"Status Code: {response.status_code}")
    if 'Allow' in response.headers:
        print(f"Allowed methods: {response.headers['Allow']}")
    else:
        print("No Allow header in response")
    
    # Print CORS headers if present
    if 'Access-Control-Allow-Methods' in response.headers:
        print(f"CORS allowed methods: {response.headers['Access-Control-Allow-Methods']}")

# ----------------------
# Authentication Examples
# ----------------------
def auth_examples():
    """Examples of API authentication"""
    print("\n=== Authentication Examples ===")
    
    # Basic Authentication
    response = requests.get(
        "https://httpbin.org/basic-auth/user/pass",
        auth=("user", "pass")
    )
    print(f"Basic Auth - Status Code: {response.status_code}")
    
    # API Key Authentication
    params = {"api_key": "your_api_key_here"}
    # response = requests.get("https://api.example.com/data", params=params)
    print("API Key Auth - Include in query parameters or headers")
    
    # Bearer Token Authentication
    headers = {"Authorization": "Bearer your_token_here"}
    # response = requests.get("https://api.example.com/data", headers=headers)
    print("Bearer Token Auth - Include in Authorization header")
    
    # OAuth 2.0 (simplified example)
    headers = {"Authorization": "Bearer your_oauth_token_here"}
    # response = requests.get("https://api.example.com/data", headers=headers)
    print("OAuth 2.0 - Similar to Bearer token after obtaining access token")

# ----------------------
# Handling Responses
# ----------------------
def response_handling():
    """Examples of handling different response types"""
    print("\n=== Response Handling Examples ===")
    
    # JSON response
    response = requests.get(f"{BASE_URL}/posts/1")
    print(f"JSON response: {response.json()['title']}")
    
    # Text response
    response = requests.get("https://httpbin.org/html")
    print(f"Text content type: {response.headers['Content-Type']}")
    print(f"Text sample: {response.text[:50]}...")
    
    # Binary response (like an image)
    response = requests.get("https://httpbin.org/image/png")
    print(f"Binary content type: {response.headers['Content-Type']}")
    print(f"Binary content length: {len(response.content)} bytes")
    
    # Error handling
    try:
        response = requests.get("https://httpbin.org/status/404")
        response.raise_for_status()  # Raises an exception for 4XX/5XX responses
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    
    # Timeouts
    try:
        response = requests.get("https://httpbin.org/delay/2", timeout=1)
    except requests.exceptions.Timeout:
        print("Request timed out")

# ----------------------
# Session Example
# ----------------------
def session_example():
    """Using a session for multiple requests"""
    print("\n=== Session Example ===")
    
    # Create a session
    session = requests.Session()
    
    # Set default headers, cookies, etc.
    session.headers.update({"User-Agent": "My Python REST Client"})
    
    # Make multiple requests with the session
    response1 = session.get(f"{BASE_URL}/posts/1")
    print(f"First session request - Status Code: {response1.status_code}")
    
    response2 = session.get(f"{BASE_URL}/posts/2")
    print(f"Second session request - Status Code: {response2.status_code}")
    
    # Close the session when done
    session.close()

# Run all examples
if __name__ == "__main__":
    pokemon('clefairy')
    #get_example()
    #post_example()
    #put_example()
    #patch_example()
    #delete_example()
    #head_example()
    #options_example()
    #auth_examples()
    #response_handling()
    #session_example()