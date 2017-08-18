import requests
import json
import sys

url = 'https://api.chucknorris.io/jokes/';

def get_categories():
    r=requests.get(url + 'categories')
    check_response(r)
    body = r.content
    response = json.loads(body)
    return response

def check_response(r):
    if(str(r).upper() != '<RESPONSE [200]>'):
        response = json.loads(r.content)
        message = response['message']
        print(message)
        sys.exit()

if(len(sys.argv) > 1):
    if( (sys.argv[1] == 'help') or (sys.argv[1] == '-h') or
            (sys.argv[1] == '--help') ):
        print('Prints a random Chack Norris joke.')
        print('Usage:')
        print('\t' + sys.argv[0] + ' [CATEGORY]' + '\t a random joke (from category if specified)')
        print('\t' + sys.argv[0] + ' categories' + '\t a list of categories')
        print('\t' + sys.argv[0] + ' help|--help|-h' + '\t prints this help')
        sys.exit()
    categories = get_categories()
    if(sys.argv[1] == 'categories'):
        for cat in categories:
            print(cat)
        sys.exit()
    if(sys.argv[1] in categories):
        category = 'random?category=' + sys.argv[1]
    else:
        print('No ' + sys.argv[1] + ' category.')
        print('Have a random joke intead:\n')

if('category' not in globals()):
    category = 'random'

r=requests.get(url + category)
check_response(r)
body = r.content
response = json.loads(body)
joke = response['value']
print(joke)
