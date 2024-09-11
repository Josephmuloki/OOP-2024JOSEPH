class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def read(self):
        return f"Reading '{self.title}' by {self.author}."

    def bookmark(self, page):
        if page <= self.pages:
            return f"Bookmarked page {page} in '{self.title}'."
        else:
            return "Invalid page number."

# Example usage
book = Book("1984", "George Orwell", 328)
print(book.read())            
print(book.bookmark(100))   
