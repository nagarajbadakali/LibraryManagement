from admin import Admin
from library import Library
from book import Book
from person import Member

# Sample admin credentials
admin1 = Admin("Ramji", "A001")
library = Library("NRB Public Library")


# Main menu loop
def main():
    logged_as_member = None
    print("\n📚 Welcome to NRB Library Management System\n")
    while True:
        print("\n What you want ??")
        print("1. Admin Login")
        print("2. Add Book")
        print("3. Remove Book")
        print("4. Register Member")
        print("5. Remove Member")
        print("6. Display Books")
        print("7. Display Members")
        print("8. Find book by title")
        print("9. Find member by ID")
        print("10. Login as a member")
        print("11. Borrow book")
        print("12. Return book")
        print("13. Member Logout")
        print("14. Logout")
        print("15. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            password = input("Enter Admin Password: ")
            admin1.login(password)

        elif choice == "2":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")
            book = Book(title, author, isbn)
            admin1.add_book_to_library(library, book)

        elif choice == "3":
            title = input("Enter title of book to remove: ")
            admin1.remove_book_from_library(library, title)

        elif choice == "4":
            name = input("Enter member name: ")
            pid = input("Enter member ID: ")
            member = Member(name, pid)
            admin1.register_member_to_library(library, member)

        elif choice == "5":
            pid = input("Enter member ID to remove: ")
            admin1.remove_member_from_library(library, pid)

        elif choice == "6":
            library.display_books()

        elif choice == "7":
            library.display_members()

        elif choice == "8":
            title = input("Enter title of book to search: ")
            print(library.find_book_by_title(title))

        elif choice == "9":
            member_id = input("Enter member id to search: ")
            print(library.find_member_by_id(member_id))

        elif choice == "10":
            pid = input("Enter member id")
            member = library.find_member_by_id(pid)
            if member:
                logged_as_member = member
                print(f"✅ Member {member.name} logged in.")
            else:
                print("❌ Member not found.")

        elif choice == "11":
            if not logged_as_member:
                print("Pls login as a member")
            else:
                title = input("Enter book title name: ")
                book = library.find_book_by_title(title)
                if book:
                    logged_as_member.borrow_book(book)
                else:
                    print("Book not found")
        elif choice == "12":
            if not logged_as_member:
                print("Pls login as a member")
            else:
                title = input("Enter book title name: ")
                book = library.find_book_by_title(title)
                if book:
                    logged_as_member.return_book(book)
                else:
                    print("Book not found")

        elif choice == "13":
            if logged_as_member:
                print(f"✅ Member {logged_as_member.name} logged out.")
                logged_as_member = None
            else:
                print("❌ No member is currently logged in.")


        elif choice == "14":
            admin1.logout()

        elif choice == "15":
            print("Exiting... Goodbye!")
            break

        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
