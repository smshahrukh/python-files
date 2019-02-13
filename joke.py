import random
import requests
from flask import Flask

app = Flask(__name__)

# id to joke
jokes = {}

def _build_html(joke, joke_id):
    joke = '<div> %s </div> ' % joke
    joke_url = '<div> http://127.0.0.1:5000/%d </div>' % joke_id
    return joke + joke_url

@app.route("/")
def get_joke():
    request = requests.get('http://absum.is:5000/api/joke')
    if request.status_code > 400:  # any bad request
        joke_id = random.choice(jokes.keys())
        joke = jokes[joke_id]
        return _build_html(joke, joke_id)
    response_content = request.json()
    joke = response_content['value']['joke']
    joke_id = response_content['value']['id']
    jokes[joke_id] = joke
    return _build_html(joke, joke_id)

def _get_joke_id(joke_id, retry_amount=0):
    request = requests.get('http://absum.is:5000/api/joke/%d' % joke_id)
    if request.status_code > 500:
        # doesn't exist in our dictionary and server errors
        # retry
        if not jokes.get(joke_id) and retry_amount < 3:
            return _get_joke_id(joke_id, retry_amount + 1)
    elif request.status_code >= 400:
        return '<div> knock knock, whos there, europe, europe who? no ur a poo </div>'
    response_content = request.json()
    return  response_content['value']['joke']


@app.route("/<int:joke_id>")
def get_joke_id(joke_id):
    return _get_joke_id(joke_id)

if __name__ == "__main__":
    app.run(debug=True)