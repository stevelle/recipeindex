import pytest

import main


@pytest.fixture
def test_app():
    main.app.testing = True
    main.app.config['WTF_CSRF_ENABLED'] = False
    return main.app.test_client()


def test_get_books_add(test_app):
    r = test_app.get('/books/add')

    assert r.status_code == 200


def test_post_books_add(test_app):
    r = test_app.post('/books/add', data={'isbn': '1234567890',
                                          'submit': 'Save'})
    assert r.status_code == 200
