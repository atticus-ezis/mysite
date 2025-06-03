from django.contrib import admin

from books.models import Author, Book, Publisher, Classification

class AuthorAdmin(admin.ModelAdmin):
    fields = ["email", "first_name", "last_name"]
    search_fields = ["first_name", "last_name"] # added search field 

class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["classification", "title", "authors", "publisher"]}), # re-ordered fields in change form
        ("Date information", {
            "fields": ["publication_date"],
            "classes": ["collapse"],
        }),

    ]
    list_display = ["title", "publisher", "was_published_recently"]
    search_fields = ['title']
    filter_horizontal = ['authors']

class BookInline(admin.TabularInline):
    model = Book
    extra = 3

class PublisherAdmin(admin.ModelAdmin):
    inlines = [BookInline]
    fields = ["website", "name", "address", "city", "country"] # re-order fields in change form
    search_fields = ["name", "city", "country", "website"] # added search field 
    list_display = ["name", "city", "country", "website"] # add display list

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Classification)