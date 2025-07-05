from person import Person


class Admin(Person):
    _admin_credentials = {
        "A001": "admin123",  # ID: password
        "A002": "secret456"
    }

    def __init__(self, name, person_id):
        super().__init__(name, person_id)
        self.logged_in = False

    def get_details(self):
        return f"Admin {self.name}, ID {self.person_id}"

    def login(self, password):
        if Admin._admin_credentials.get(self.person_id) == password:
            self.logged_in = True
            print(f"Admin {self.name} logged in successfully")
        else:
            print("Invalid credentials")


    def require_login(func):
        def wrapper(self, *args, **kwargs):
            if not self.logged_in:
                print("❌ Access denied. Please login as Admin first.")
                return
            return func(self, *args, **kwargs)
        return wrapper
    @require_login
    def add_book_to_library(self, library, book):
        library._add_book(book)

    @require_login
    def remove_book_from_library(self, library, book):
        library._remove_book(book)

    @require_login
    def register_member_to_library(self, library, member):
        library._register_member(member)

    @require_login
    def remove_member_from_library(self, library, member_id):
        library._remove_member(member_id)
    @require_login
    def logout(self):
        self.logged_in =False
        print(f"Admin {self.name} logged out successfully")