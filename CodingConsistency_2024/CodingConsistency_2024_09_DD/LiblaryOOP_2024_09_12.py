class Liblary:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f"Book {book} is added to liblary")
    
    def book_listings(self):
        if not self.books:
            print("No books here")
        else:
            for book in self.books:
                print(f"- {book}")

obj = Liblary()

obj.add_book("Testing1")
obj.add_book("Testing2")
obj.add_book("Testing3")

obj.book_listings()

