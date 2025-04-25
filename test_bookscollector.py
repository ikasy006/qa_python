import pytest

from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self, book_collector_with_books):
        assert len(book_collector_with_books.get_books_genre()) == 3


    @pytest.mark.parametrize('name', ['', 'сорок коров лежали на лугу и жевали траву'])
    def test_add_new_book_name_of_false(self, book_collector_create, name):
        book_collector_create.add_new_book(name)
        assert len(book_collector_create.get_books_genre()) == 0

    def test_default_value_books_genre_true(self, book_collector_create):
        assert len(book_collector_create.get_books_genre()) == 0

    def test_default_value_favorites(self, book_collector_create):
        assert len(book_collector_create.get_list_of_favorites_books()) == 0

    @pytest.mark.parametrize("genre, expected_genre", [
                                ('Фантастика', 'Фантастика'),
                                ('NN жанр', '')])
    def test_set_book_genre_true(self, book_collector_with_books, genre, expected_genre):
        book_collector_with_books.set_book_genre("Book1", genre)
        assert book_collector_with_books.get_book_genre("Book1") == expected_genre

    @pytest.mark.parametrize('name, genre', [
                                ("Book1", "Фантастика"),
                                ("Book2", "Ужасы"),
                                ("Book3", "Комедии")])
    def test_get_book_genre_true(self, name, genre, book_collector_with_genres):
        assert book_collector_with_genres.get_book_genre(name) == genre

    def test_get_books_with_specific_genre_found(self, book_collector_with_genres):
        assert book_collector_with_genres.get_books_with_specific_genre("Фантастика") == ["Book1"]

    def test_get_books_with_specific_genre_not_found(self, book_collector_with_genres):
        assert book_collector_with_genres.get_books_with_specific_genre("NN жанр") == []

    def test_get_books_genre(self, book_collector_with_genres):
        expected = {"Book1": "Фантастика", "Book2": "Ужасы", "Book3": "Комедии"}
        assert book_collector_with_genres.get_books_genre() == expected

    def test_get_books_for_children_true(self, book_collector_with_genres):
        expected = ["Book1", "Book3"]
        assert book_collector_with_genres.get_books_for_children() == expected

    def test_add_book_in_favorites_no_duplicates(self, book_collector_with_favorites):
        book_collector_with_favorites.add_book_in_favorites("Book1")
        assert len(book_collector_with_favorites.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_existing(self, book_collector_with_favorites):
        book_collector_with_favorites.delete_book_from_favorites("Book1")
        assert len(book_collector_with_favorites.get_list_of_favorites_books()) == 0

    def test_get_list_of_favorites_books_existing(self, book_collector_with_favorites):
        expected = ["Book1"]
        assert book_collector_with_favorites.get_list_of_favorites_books() == expected
