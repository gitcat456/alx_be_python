class Book:
    def __init__(self, title, author):
        self.title = title              
        self.author = author            
        self._is_checked_out = False    

    def check_out(self):
        """Marks the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marks the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Checks if the book is currently available."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []  

    def add_book(self, book):
        """Adds a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Finds the book by title and checks it out if available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
       

    def return_book(self, title):
        """Finds the book by title and marks it as returned."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return

    def list_available_books(self):
        """Prints all books that are currently available."""
        available_books = [book for book in self._books if book.is_available()]
        for book in available_books:
            print(f"{book.title} by {book.author}")