from task1_lab2 import Book

BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    },
]


class Library:
    """Класс для представления библиотеки книг."""

    def __init__(self, books: list[Book] = None):
        """
        Инициализация библиотеки.

        :param books: Список книг (по умолчанию пустой список)
        """
        self.books = books if books is not None else []

    def get_next_book_id(self) -> int:
        """Возвращает идентификатор для следующей книги."""
        return len(self.books) + 1 if self.books else 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Возвращает индекс книги по её идентификатору.

        :param book_id: Идентификатор книги
        :raises ValueError: Если книги с таким id не существует
        :return: Индекс книги
        """
        for index, book in enumerate(self.books):
            if book.id_ == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # Инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # Проверяем следующий id

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # Инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # Проверяем следующий id

    print(library_with_books.get_index_by_book_id(1))  # Проверяем индекс книги с id=1
