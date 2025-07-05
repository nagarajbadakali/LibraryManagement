from book import Book
from person import Member
from library import Library
from admin import Admin

admin1 = Admin("Ramji", "A001")
admin1.login("admin123")

my_library = Library("NRB public library")

# Add Books
book1 = Book("Atomic Habits", "James Clear", "9780735211292")
book2 = Book("Deep Work", "Cal Newport", "9781455586691")
book3 = Book("The Alchemist", "Paulo Coelho", "9780061122415")

admin1.add_book_to_library(my_library, book1)
admin1.add_book_to_library(my_library, book2)
admin1.add_book_to_library(my_library, book3)

# Register Members
member1 = Member("Nagaraj", "M001")
member2 = Member("Akash", "M002")

admin1.register_member_to_library(my_library, member1)
admin1.register_member_to_library(my_library, member2)

my_library.display_books()
member1.borrow_book(book1)
my_library.display_books()

member1.return_book(book1)
my_library.display_books()
my_library.display_members()
