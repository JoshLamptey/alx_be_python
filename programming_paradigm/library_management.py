class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.is_checked_out = False

    
# method for checking out 
    
    def check_out(self):
        self.is_checked_out = True

    #method for returning a book
    def return_book(self):
        self.is_checked_out = False

    # method to indicate whether a book is available
    def is_available(self):
        return not self.is_checked_out
    

# Library Class

class Library:
    def __init__(self):
        self.books = []

    #method for adding books 
    def add_book(self,book):
        self.books.append(book)


    #method for checking out books
    def check_out_book(self,title):
        for book in self.books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"Checked out '{title}'")
            else:
                print(f"Book {title} has been checked out or does not exist.")



               
    #method for returning books 
    def return_book(self,title):
        for book in self.books:
            if book.title == title and not book.is_available():
                book.return_book()
            else:
                print(f"Book '{title}' was not checked out or does not exist.")


    #method to list out available books 
    def list_available_books(self):
        available_books = [book for book in self.books if book.is_available()]
        if not available_books:
            print('No books are currently available')
        else:
            for book in available_books:
                print(f"{book.title} by {book.author}")
