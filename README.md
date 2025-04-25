# qa_python

test_add_new_book_add_two_books - добавление книг в словарь books_genre (исходный тест)
test_add_new_book_name_of_false - добавление книги с некорректным названием в словарь books_genre не осуществилось
test_default_value_books_genre_true - дефолное значение словаря книг books_genre (при инициализации в конструкторе)
test_default_value_favorites - дефолное значение избранных словаря книг favorites(при инициализации в конструкторе)
test_set_book_genre_true - жанр книги устанавливается
test_get_book_genre_true - вывод жанра книг по названию
test_get_books_with_specific_genre_not_found - книги несуществующего (в списке жанров) жанра отсутствуют
test_get_books_genre - получение текущего словаря books_genre.
test_get_books_for_children_true - получение книг, подходящих детям (отсутствуют в списке жанров с ограничением genre_age_rating)
test_add_book_in_favorites_no_duplicates - добавление дубликатов в список избранных книг (favorites) не осуществляется
test_delete_book_from_favorites_existing - книги из списка избранных книг (favorites) можно удалить
test_get_list_of_favorites_books_existing - получение списка избранных книг (favorites)
