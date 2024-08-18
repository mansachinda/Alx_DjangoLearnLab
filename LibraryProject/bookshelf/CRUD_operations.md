CRUD OPERATIONS IN DJANGO SHELL
-------------------------------------------------------------------------------------------------

from bookshelf.models import Book

Create Book
book = Book.objects.create(title="1984", author="George Orwell",publication_year=1949)

output:

<Book: Book object (2)>
--------------------------------------------------------------------------------------------------

Retrieve Book
Book.objects.get(title="1984")
--------------------------------------------------------------------------------------------------

Update Book
book.title = “Nineteen Eighty-Four”
book.save()
--------------------------------------------------------------------------------------------------

Delete Book
book.delete()

output:
(1, {'bookshelf.Book': 1})
