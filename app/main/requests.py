import urllib.request,json
from .model import Post
import requests
def configure_request(app):
    global base_url
    base_url = app.config['BASE_URL']


def new_book(endpoint, post):
    posts_url = base_url.format(endpoint)
    result=requests.post(posts_url, json=post)



def get_books(endpoint):
    '''
    Function that gets the json response to our url request
    '''
    get_post_url = base_url.format(endpoint)
    print(get_post_url)
    with urllib.request.urlopen(get_post_url) as url:
        get_data = url.read()
        response = json.loads(get_data)
        if response['data']:
            results = response['data']
    return results

def get_one_book(endpoint):
    url = base_url.format(endpoint)
    result = requests.get(url).json()
    if result['todo']:
        post = result['todo']
    return post

def get_random_quote():
    quote_url ='http://quotes.stormconsultancy.co.uk/random.json'
    quote = requests.get(quote_url).json()
    return quote
