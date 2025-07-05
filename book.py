class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Not Available"
        return f"{self.title}  by {self.author} (ISBN: {self.isbn}) - {status}"
    
