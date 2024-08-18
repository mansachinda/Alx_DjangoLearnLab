from .models import Author, Book, Library, Librarian

# This is where we Add Author objects
steven = Author.objects.create(name="Steven Bartlett")
steven.save()
robert = Author.objects.create(name="Robert Greene")
robert.save()
author_name = Author.objects.create(name='Author Name')

# This is where we Add Book objects
the = Book.objects.create(title="The Diary of a CEO", author=steven) 
mastery = Book.objects.create(title="Mastery", author=robert)

the.save()
mastery.save()

# This is to Get books by each author
Book.objects.get(author=robert) 
Book.objects.get(author=steven)
Author.objects.get(name=author_name)
Author.objects.filter(author=author)

# This will List all books
Book.objects.all()

# This is used to Create Library Instance
sandtech = Library.objects.create(name='sandtech')
sandtech.save()

# This will allow us Add books to Library
sandtech.books.add(the, mastery)

# This will List all books in Library
sandtech.books.all()
Library.objects.get(name=library_name)

# This allows us to Add Librarian
lynn = Librarian.objects.create(name='Lynn Nungari', library=sandtech)
lynn.save()

# This allows us Retrieve a Librarian for a library
lynn.library
Librarian.objects.get(library=sandtech)
