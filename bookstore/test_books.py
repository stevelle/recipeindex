from unittest.mock import ANY, patch

import pytest
import responses

import books
from common_testing import MINIMAL, openlib_url


@responses.activate
def test_lookup_isbn_basic():
    responses.add(responses.GET, openlib_url('1234567890'),
                  json=MINIMAL, status=200)

    data = books.lookup_isbn('1234567890')
    assert 'Minimal Title' in data['first'].values()


@responses.activate
def test_lookup_isbn_fails():
    responses.add(responses.GET, openlib_url('1234567890'),
                  body=IOError('Boom!'))

    with pytest.raises(IOError):
        books.lookup_isbn('1234567890')


@responses.activate
def test_lookup_isbn_missing():
    responses.add(responses.GET, openlib_url('1234567890'),
                  json={}, status=200)

    data = books.lookup_isbn('1234567890')
    assert data == {}


@patch('books.client')
def test_add_book_basic(mocked_client):
    returned = books.add_book(MINIMAL)

    assert returned['title'] == MINIMAL['first']['title']
    assert MINIMAL['first']['url'].endswith(returned['url'])
    assert 'http' not in returned['url']
    mocked_client.key.assert_called_once_with('Book', '6666666666')
    mocked_client.put.assert_called_once_with(ANY)


@patch('books.client')
def test_add_book_with_subtitle(mocked_client):
    input = MINIMAL
    input['first'].update({'subtitle': 'the subtext returns'})

    returned = books.add_book(input)

    assert returned['subtitle'] == 'the subtext returns'
    mocked_client.key.assert_called_once_with('Book', '6666666666')
    mocked_client.put.assert_called_once_with(ANY)


@patch('books.client')
def test_add_book_with_isbn_13(mocked_client):
    input = MINIMAL
    input['first']['identifiers'].update({'isbn_13': ['9871234567890']})

    returned = books.add_book(input)

    assert returned['isbn13'] == '9871234567890'
    mocked_client.key.assert_called_once_with('Book', '6666666666')
    mocked_client.put.assert_called_once_with(ANY)


@patch('books.client')
def test_add_book_with_authors(mocked_client):
    input = MINIMAL
    input['first'].update({'authors': [
            {
                'name': 'Some Juan',
                'url': 'https://openlibrary.org/authors/6666666666/Some_Juan'
            }
        ]})

    returned = books.add_book(input)

    assert returned['authors'] == ['Some Juan']
    mocked_client.key.assert_called_once_with('Book', '6666666666')
    mocked_client.put.assert_called_once_with(ANY)


@patch('books.client')
def test_add_book_with_subjects(mocked_client):
    input = MINIMAL
    input['first'].update({'subjects': [
            {
                'name': 'Being Smart',
                'url': 'https://openlibrary.org/subjects/being_smart'
            },
            {
                'name': 'Getting Good Grades',
                'url': 'https://openlibrary.org/subjects/getting_good_grades'
            }
        ]})

    returned = books.add_book(input)

    assert 'Being Smart' in returned['subjects']
    assert 'Getting Good Grades' in returned['subjects']
    mocked_client.key.assert_called_once_with('Book', '6666666666')
    mocked_client.put.assert_called_once_with(ANY)


@patch('books.client')
def test_add_book_with_covers(mocked_client):
    input = MINIMAL
    input['first'].update({'cover': {
            'large': 'https://covers.openlibrary.org/b/id/123456-L.jpg',
            'medium': 'https://covers.openlibrary.org/b/id/123456-M.jpg',
            'small': 'https://covers.openlibrary.org/b/id/123456-S.jpg'
        }})

    returned = books.add_book(input)

    assert 3 == len(returned['covers'])
    assert 'covers.openlibrary.org/b/id/123456-M.jpg' in returned['covers']
    mocked_client.key.assert_called_once_with('Book', '6666666666')
    mocked_client.put.assert_called_once_with(ANY)
