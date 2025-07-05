from book import Book
from person import Member
member1 = Member("Nagaraj","M001")

book1 = Book("Atomic Habits", "James Clear", "9780735211292")
book2 = Book("Deep Work", "Cal Newport", "9781455586691")
member1.borrow_book(book1)
member1.borrow_book(book2)
print(member1.get_details())

member1.return_book(book1)
print(member1.get_details())
print(book1)
