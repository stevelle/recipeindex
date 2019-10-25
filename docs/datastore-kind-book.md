# Storage schema :: Book
This describes a schema for the "Book" Kind for storage in Firestore Cloud (DataStore Mode).

Properties:
  * title
  * subtitle
  * authors (0..n)
  * subjects
  * isbn13
  * isbn10 (key)
  * covers (0..3)
  * url (at openlibrary.org)

Indexes:

All of the following properties should be indexed

  * title
  * subtitle
  * authors
  * subjects
  * isbn13

## Example of creating a Book with this schema
```
from google.cloud import datastore

# [...]

isbn_13 = as_isbn_13(isbn)
isbn_10 = as_isbn_10(isbn)

# [...]

client = datastore.Client()

book = datastore.Entity(client.key('Book', isbn_10),
    exclude_from_indexes=['covers', 'url'])
book.update({
    'title': 'a book',
    'subtitle': 'the subtitle',
    'authors': ['author, name', 'other, name'],
    'subjects': ['sub-1', 'sub-2', 'sub-3'],
    'isbn13': isbn13,
    'covers': ['small-img', 'medium-img', 'large-img'],
    'url': 'at.internet.archive/'
})
client.put(book)
```
