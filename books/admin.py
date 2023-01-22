from django.contrib import admin

from books.models import Book, BookAuthor, Review, Author

admin.site.register(Book)
admin.site.register(BookAuthor)
admin.site.register(Author)
admin.site.register(Review)
