from admin import Admin
from library import Library
from book import Book
from person import Member

# Setup
admin1 = Admin("Ramji", "A001")
library = Library("NRB Public Library")

def main():
    logged_as_member = None
    print("\n📚 Welcome to NRB Library Management System 📚")
    print("=============================================")

    while True:
        print("\n🏠 Main Menu:")
        print("1️⃣  Admin Panel")
        print("2️⃣  Member Panel")
        print("3️⃣  General Operations")
        print("4️⃣  Exit")

        choice = input("👉 Enter your choice: ").strip()

        # ===================== ADMIN PANEL =====================
        if choice == "1":
            while True:
                print("\n🔐 Admin Panel:")
                print("1. Login")
                print("2. Add Book")
                print("3. Remove Book")
                print("4. Register Member")
                print("5. Remove Member")
                print("6. Logout")
                print("7. Back to Main Menu")

                admin_choice = input("🛠️  Choose an option: ").strip()

                if admin_choice == "1":
                    password = input("Enter Admin Password: ").strip()
                    admin1.login(password)

                elif admin_choice == "2":
                    if not admin1.logged_in:
                        print("❌ Please login first.")
                        continue
                    title = input("Book title: ").strip()
                    author = input("Author: ").strip()
                    isbn = input("ISBN: ").strip()
                    book = Book(title, author, isbn)
                    admin1.add_book_to_library(library, book)

                elif admin_choice == "3":
                    if not admin1.logged_in:
                        print("❌ Please login first.")
                        continue
                    title = input("Book title to remove: ").strip()
                    admin1.remove_book_from_library(library, title)

                elif admin_choice == "4":
                    if not admin1.logged_in:
                        print("❌ Please login first.")
                        continue
                    name = input("Member name: ").strip()
                    pid = input("Member ID: ").strip()
                    member = Member(name, pid)
                    admin1.register_member_to_library(library, member)

                elif admin_choice == "5":
                    if not admin1.logged_in:
                        print("❌ Please login first.")
                        continue
                    pid = input("Member ID to remove: ").strip()
                    admin1.remove_member_from_library(library, pid)

                elif admin_choice == "6":
                    admin1.logout()

                elif admin_choice == "7":
                    break

                else:
                    print("❌ Invalid admin choice.")

        # ===================== MEMBER PANEL =====================
        elif choice == "2":
            while True:
                print("\n👤 Member Panel:")
                print("1. Login")
                print("2. Borrow Book")
                print("3. Return Book")
                print("4. Logout")
                print("5. Back to Main Menu")

                member_choice = input("📘 Choose an option: ").strip()

                if member_choice == "1":
                    pid = input("Enter member ID: ").strip()
                    member = library.find_member_by_id(pid)
                    if member:
                        logged_as_member = member
                        print(f"✅ Member '{member.name}' logged in.")
                    else:
                        print("❌ Member not found.")

                elif member_choice == "2":
                    if not logged_as_member:
                        print("❌ Login as a member first.")
                        continue
                    title = input("Book title to borrow: ").strip()
                    book = library.find_book_by_title(title)
                    if book:
                        logged_as_member.borrow_book(book)
                    else:
                        print("❌ Book not found.")

                elif member_choice == "3":
                    if not logged_as_member:
                        print("❌ Login as a member first.")
                        continue
                    title = input("Book title to return: ").strip()
                    book = library.find_book_by_title(title)
                    if book:
                        logged_as_member.return_book(book)
                    else:
                        print("❌ Book not found.")

                elif member_choice == "4":
                    if logged_as_member:
                        print(f"👋 Member '{logged_as_member.name}' logged out.")
                        logged_as_member = None
                    else:
                        print("⚠️  No member is logged in.")

                elif member_choice == "5":
                    break

                else:
                    print("❌ Invalid member choice.")

        # ===================== GENERAL OPERATIONS =====================
        elif choice == "3":
            while True:
                print("\n📋 General Operations:")
                print("1. Display All Books")
                print("2. Display All Members")
                print("3. Search Book by Title")
                print("4. Search Member by ID")
                print("5. Back to Main Menu")

                general_choice = input("🔎 Choose an option: ").strip()

                if general_choice == "1":
                    library.display_books()

                elif general_choice == "2":
                    library.display_members()

                elif general_choice == "3":
                    title = input("Book title to search: ").strip()
                    print(library.find_book_by_title(title))

                elif general_choice == "4":
                    pid = input("Member ID to search: ").strip()
                    print(library.find_member_by_id(pid))

                elif general_choice == "5":
                    break

                else:
                    print("❌ Invalid option.")

        # ===================== EXIT =====================
        elif choice == "4":
            print("👋 Goodbye! Thanks for using NRB Library.")
            break

        else:
            print("❌ Invalid main menu choice. Please try again.")

if __name__ == "__main__":
    main()
