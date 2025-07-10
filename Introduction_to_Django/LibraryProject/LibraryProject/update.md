from bookshelf.models import Book
# Update the title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
# Confirm the change
book = Book.objects.get(id=book.id)
book.title
# Expected shell output:
# 'Nineteen Eighty-Four'
