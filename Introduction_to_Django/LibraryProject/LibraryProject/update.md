
#### 📄 `update.md`
```markdown
```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Confirm update
book = Book.objects.get(id=book.id)
book.title
# 'Nineteen Eighty-Four'
