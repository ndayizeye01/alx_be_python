class Book:
    def __init__(self, title:str, author:str):
        self.title = title
        self.author = author


class EBook(Book):
    def __init__(self, title, author, file_size:int):
        super().__init__(title, author)
        self.file_size = file_size

class PrintBook(Book):
    def __init__(self, title, author, page_count:int):
        super().__init__(title, author)
        self.page_count = page_count

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        return self.books.append(book)
    def list_books(self):
        for book in self.books:
            if type(book).__name__ == "Book":
                print(f"Book: {book.title} by {book.author}")
            elif type(book).__name__ == "EBook":
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif type(book).__name__ == "PrintBook":
                print(f"PrintBook: {book.title} by {book.author}, Page count: {book.page_count}")

    
        