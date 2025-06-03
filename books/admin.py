from django.contrib import admin

# Register your models here.
from books.models import Author, Book, Publisher, Classification

# changes order
class AuthorAdmin(admin.ModelAdmin):
    fields = ["email", "first_name", "last_name"]

class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["title", "authors", "publisher", "classification"]}),
        ("Date information", {
            "fields": ["publication_date"],
            "classes": ["collapse"],
        }),

    ]
    list_display = ["title", "publisher"]

class BookInline(admin.StackedInline):
    model = Book
    extra = 3

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Publisher)
admin.site.register(Classification)