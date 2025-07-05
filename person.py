from abc import ABC, abstractmethod
from book import Book


class Person(ABC):
    def __init__(self, name, person_id):
        self.name = name
        self.person_id = person_id

    @abstractmethod
    def get_details(self):
        pass


class Member(Person):
    def __init__(self, name, person_id):
        super().__init__(name, person_id)
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            self.borrowed_books.append(book)
            book.available = False
            print(f"{self.name} has borrowed {book.title}")
        else:
            print(f"Sorry {book.title} is not available")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.available = True
            print(f"{self.name} has returned the {book.title}")
        else:
            print(f"{self.name} has not borrowed the {book.title}")

    def get_details(self):
        book_list = ",".join([book.title for book in self.borrowed_books]) or f"No books borrowed "
        return f"Member: {self.name}, ID : {self.person_id}, Books : {book_list}"
