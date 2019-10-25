from google.cloud import datastore
import requests

INVALID_ISBN_MSG = 'ISBN: {} is either not valid or unknown'
UNINDEXED_ATTRIBUTES = ['covers', 'url']
OPEN_LIBRARY_URL = ('https://openlibrary.org/api/books?' +
                    'bibkeys=ISBN:{isbn}&format=json&jscmd=data')

__client = None


def add_book(book_data):
    # TODO What if there are multiple matches? or none?
    props = list(book_data.values())[0]

    isbn = props.get('identifiers').get('isbn_10')[0]

    attributes = {
        'title': props.get('title'),
        'url': props.get('url')[8:]
    }

    if 'subtitle' in props:
        attributes.update({'subtitle': props.get('subtitle')})

    if 'identifiers' in props and 'isbn_13' in props.get('identifiers'):
        isbn13 = props.get('identifiers').get('isbn_13')[0]
        attributes.update({'isbn13': isbn13})

    if 'authors' in props:
        authors = [author.get('name') for author in props.get('authors')]
        attributes.update({'authors': authors})

    if 'subjects' in props:
        subjects = [sub.get('name') for sub in props.get('subjects')]
        attributes.update({'subjects': subjects})

    if 'cover' in props:
        cover_urls = [url[8:] for url in props.get('cover').values()]
        attributes.update({'covers': cover_urls})

    key = client.key('Book', isbn)
    book = datastore.Entity(key, exclude_from_indexes=UNINDEXED_ATTRIBUTES)
    book.update()

    client.put(book)
    return attributes


def lookup_isbn(isbn):
    r = requests.get(OPEN_LIBRARY_URL.format(isbn=isbn))
    r.raise_for_status()
    return r.json()


def client():
    global __client
    if not __client:
        __client = datastore.Client()
    return __client
