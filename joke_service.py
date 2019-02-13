
JOKE_API_URL = 'http://absum.is:5000/api/joke'

import bottle
import json
import random
import requests

joke_storage = {}

@bottle.get('/joke/')
@bottle.get('/joke')
@bottle.get('/joke/<joke_id>')
def joke(joke_id=None):

    if joke_id:
        url = '{}/{}'.format(JOKE_API_URL, joke_id)
    else:
        url = JOKE_API_URL

    if joke_id in joke_storage:
        return '{}\n'.format(joke_storage[joke_id])
    else:
        request = requests.get(url)
        if request.ok:
            try:
                return_object = json.loads(request.text)
                joke = return_object['value']['joke']
                joke_id = str(return_object['value']['id'])
                print(joke_id)
            except json.decoder.JSONDecodeError as e:
                return "Don't hire interns, ever.\n"
            except KeyError:
                return "Joke Not Found.  Perhaps you should look in the mirror.\n"
            else:
                joke_storage[joke_id] = joke
                return '{}\n'.format(joke)
        elif joke_id is None:
            return '{}\n'.format(random.choice([_ for _ in joke_storage.values()]))
        else:
            return "Service unreacheable ::: {}\n".format(request.status_code)

if __name__ == '__main__':
    bottle.run(host='localhost', port=5050, debug=True)