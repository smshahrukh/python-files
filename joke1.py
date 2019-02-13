JOKE_API_URL = 'http://absum.is:5000/api/joke'

import requests
import docopt
import json
import bottle

def main(arguments):
    """
    """
    # acquire joke ID
    joke_id = arguments['<joke_id>']

    if joke_id:
        url = '{}/{}'.format(JOKE_API_URL, joke_id)
    else:
        url = JOKE_API_URL

    request = requests.get(url)
    if request.ok:
        try:
            joke = json.loads(request.text)['value']['joke']
        except json.decoder.JSONDecodeError as e:
            print("Don't hire interns, ever.")
        except KeyError:
            print("Joke Not Found.  Perhaps you should look in the mirror.")
        else:
            print(joke)
    else:
        print("Service unreacheable ::: {}".format(request.status_code))

if __name__ == '__main__':
    arguments = docopt.docopt(__doc__)
    main(arguments)