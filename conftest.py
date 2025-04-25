import pytest

from main import BooksCollector


@pytest.fixture
def book_collector_create():
    return BooksCollector()

@pytest.fixture
def book_collector_with_books(book_collector_create):
    book_collector_create.add_new_book("Book1")
    book_collector_create.add_new_book("Book2")
    book_collector_create.add_new_book("Book3")
    return book_collector_create

@pytest.fixture
def book_collector_with_genres(book_collector_with_books):
    book_collector_with_books.set_book_genre("Book1", "Фантастика")
    book_collector_with_books.set_book_genre("Book2", "Ужасы")
    book_collector_with_books.set_book_genre("Book3", "Комедии")
    return book_collector_with_books

@pytest.fixture
def book_collector_with_favorites(book_collector_with_books):
    book_collector_with_books.add_book_in_favorites("Book1")
    return book_collector_with_books
