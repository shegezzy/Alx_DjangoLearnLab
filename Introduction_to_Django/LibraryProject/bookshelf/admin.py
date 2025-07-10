from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Show these columns
    list_filter = ('author', 'publication_year')            # Add filter sidebar
    search_fields = ('title', 'author')                     # Enable search bar
