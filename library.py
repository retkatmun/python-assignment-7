"""
Library Management System

Task:
- Create functions to manage a library using dictionaries and lists.
- Each book is stored in a dictionary with fields: { "id": int, "title": str, "author": str, "available": bool }
- Users can borrow and return books.
- Support *args for searching books by multiple fields (title, author).
- Support **kwargs for adding optional book details like "year", "genre".


// NOT FOR THIS ASSIGNMENT
Future OOP Extension:
- Books as a Book class.
- Library as a Library class with borrow() and return() methods.
"""
library = []

def add_book(book_id, title, author, **kwargs):
    """
    Add a new book into the library with flexible details.
    return "Book {book_title} added successfully!"
    """
    library.append({"id": book_id, "title": title, "author": author, "available": True, **kwargs})
    return f"Book '{title}' added successfully"

def search_books(*args):
    """
    Search for books by multiple keywords (title, author).
    Return matching books or 'No books found.'
    """
    results = []
    for book in library:
        for keyword in args:
            if keyword.lower() in book["title"].lower() or keyword.lower() in book["author"].lower():
                results.append(book)
                break
    return results if results else "No books found"

def borrow_book(book_id):
    """
    Borrow a book if available (msg: You borrowed {book_title}).
    else-> msg: Book {book_title} not available
    """
    for b in library:
        if b["id"] == book_id:
            if b["available"]:
                b["available"] = False
                return f"You borrowed '{b['title']}'"
            return f"Book '{b['title']}' not available"
    return "Book not found."

def return_book(book_id):
    for b in library:
        if b["id"] == book_id:
            if not b["available"]:
                b["available"] = True
                return f"You returned {b['title']}"
            return f"Book {b['title']} was not borrowed"
    return "Book not found."


print(add_book(1, "Python Basics", "John mimi", year=2025, genre="Education: progrmming"))
print(search_books("Python", "john"))
print(borrow_book(1))
print(borrow_book(1))
print(return_book(1))


