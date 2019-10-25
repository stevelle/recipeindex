from unittest.mock import patch

import pytest
import responses

from common_testing import MINIMAL, openlib_url
import main


@pytest.fixture
def test_app():
    main.app.testing = True
    main.app.config['WTF_CSRF_ENABLED'] = False
    return main.app.test_client()


def test_get_books_add(test_app):
    r = test_app.get('/books/add')

    assert r.status_code == 200


@responses.activate
@patch('books.client')
def test_post_books_add(mocked_client, test_app):
    responses.add(responses.GET, openlib_url('1234567890'), json=MINIMAL,
                  status=200)

    r = test_app.post('/books/add', data={'isbn': '1234567890',
                                          'submit': 'Save'})
    assert r.status_code == 200
    assert b'ISBN saved 1234567890' in r.data
