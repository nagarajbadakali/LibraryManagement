from book import Book
from person import Member


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []

    def _add_book(self, book):
        self.books.append(book)
        print(f"Book {book.title} added to {self.name}")

    def _remove_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                print(f"Book {book_title} removed from {self.name}")
                return
        print(f"Book {book_title} not found in {self.name}")

    def _register_member(self, member):
        self.members.append(member)
        print(f"Member {member.name} registered in {self.name}")

    def _remove_member(self, member_id):
        for member in self.members:
            if member.person_id == member_id:
                self.members.remove(member)
                print(f"Member_ID {member.person_id} removed from {self.name}")
                return
        print(f"Member_ID {member_id} not found in {self.name}")

    def display_books(self):
        print(f"\nAvailable books in {self.name}: ")
        for book in self.books:
            if book.available:
                print(book)

    def display_members(self):
        print(f"\nRegistered members in {self.name}:")
        for member in self.members:
            print(member.get_details())

    def find_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
            else:
                return None

    def find_member_by_id(self, id):
        for member in self.members:
            if member.person_id == id:
                return member
            else:
                return None
