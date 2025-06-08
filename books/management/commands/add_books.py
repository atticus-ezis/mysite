# Create a custom management command that would add books
# and authors from this API endpoint - http://gutendex.com/books/

# /books?ids=11,12,13

from django.core.management.base import BaseCommand, CommandError
from books.models import Book, Author
import requests

class Command(BaseCommand):

    help = "Adds book and author from API"

    def add_arguments(self, parser):
        parser.add_argument("book_ids", nargs="+", type=int)

    def handle(self, *args, **options):
        for book_id in options['book_ids']:
            try:
                url = f'https://gutendex.com/books/?ids={book_id}'
                response = requests.get(url)
                response.raise_for_status()
                data = response.json()
                results = data.get('results')

                if not results:
                    self.stdout.write(self.style.WARNING(f"No data for book ID {book_id}"))
                    continue

                book_data = results[0]

                title = book_data.get('title', 'United')

                book_obj, created = Book.objects.get_or_create(
                    title=title,
                    defaults={
                        "publication_date":None,
                        "publisher":None,
                        "classification":None,
                    }
                )
                
                authors = book_data.get('authors', [])
                if not authors:
                    self.stdout.write(self.style.WARNING(f"No authors for book ID {book_id}"))
                    continue

                author_objs = []
                for author in authors:
                    name = author.get('name', 'Unkown, Author')
                    split_name = name.split(', ')

                    if len(split_name) == 2:
                        last_name, first_name = split_name
                    else:
                        first_name = split_name[0]
                        last_name = ''

                    author_obj, _= Author.objects.get_or_create(first_name=first_name, last_name=last_name)
                    author_objs.append(author_obj)
                
                book_obj.authors.set(author_objs)
                
                self.stdout.write(self.style.SUCCESS(f"Book '{title}' saved successfully."))

            except requests.RequestException as e:
                self.stderr.write(f"Request failed for ID {book_id}: {e}")
            except Exception as e:
                    self.stderr.write(f"Error processing ID {book_id}: {e}")




            



