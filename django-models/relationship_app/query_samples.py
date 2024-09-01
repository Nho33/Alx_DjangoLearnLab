#SELECT * FROM books WHERE author = 'Example';
#  
#Library.objects.get(name=library_name)", "books.all()
#Author.objects.get(name=author_name)", "objects.filter(author=author)
#"Librarian.objects.get(library="

# 1. Retrieve a Library object by name and get all its associated books
library = Library.objects.get(name=library_name)
books = library.book_set.all()  # If ForeignKey
# or
books = library.books.all()  # If ManyToManyField

# 2. Retrieve an Author object by name and filter books written by that author
author = Author.objects.get(name=author_name)
author_books = Book.objects.filter(author=author)

# 3. Retrieve a Librarian object by their associated library
librarian = Librarian.objects.get(library__name=library_name)
