# Create a Book Instance

```python
from bookshelf.models import Book

# Create a new book instance
book = Book.objects.create(title="1984", author="George Orwell", published_date="1949-06-08")
print(book.id)  # Expected output: ID of the newly created book
