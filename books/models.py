from django.db import models
from django.utils.translation import gettext_lazy as _
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(verbose_name="e-mail", null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name="author")

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField("books.Author", related_name="books", verbose_name=_("Authors"))
    publisher = models.ForeignKey("books.Publisher", on_delete=models.CASCADE, related_name="books", verbose_name=("Publisher"), null=True)
    publication_date = models.DateField(null=True, blank=True)
    classification = models.ForeignKey("books.Classification", on_delete=models.CASCADE, related_name="books", null=True, blank=True)

    def was_published_recently(self):
        date_today = datetime.datetime.now().date()
        publication_date = self.publication_date.date()
        return date_today - datetime.timedelta(days=1) <= publication_date <=date_today
    
    was_published_recently.admin_order_field = 'publication_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'published recently?'

    def __str__(self):
        return self.title

# Exercise 4 
class Classification(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    

