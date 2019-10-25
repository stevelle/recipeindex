import json

MINIMAL_TEXT = """
    {
        "first": {
            "identifiers": {
                "isbn_10": [
                    "6666666666"
                ]
            },
            "title": "Minimal Title",
            "url": "https://example.org/Minimal%20Title"
        }
    }
    """

MINIMAL = json.loads(MINIMAL_TEXT)


def openlib_url(isbn):
    from books import OPEN_LIBRARY_URL
    return OPEN_LIBRARY_URL.format(isbn=isbn)
