from django.db import models
from pandas import notnull

# Create your models here.


class BookJournalBase(models.Model):
    name = models.CharField(max_length=255, notnull=True)
    price = models.BigIntegerField(notnull=True)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)



class Book(BookJournalBase):
    num_pages = models.BigIntegerField()
    genre = models.CharField(max_length=255, notnull=True)

# class Journal(BookJournalBase):
#     type = models.

