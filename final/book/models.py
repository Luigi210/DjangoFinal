from django.db import models

# Create your models here.


class BookJournalBase(models.Model):
    name = models.CharField(max_length=255)
    price = models.BigIntegerField()
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)



class Book(BookJournalBase):
    num_pages = models.BigIntegerField()
    genre = models.CharField(max_length=255)

class Journal(BookJournalBase):

    type_choice = (
        ('bullet', 'Bullet'),
        ('food', 'Food'),
        ('travel', 'Travel'),
        ('sport', 'Sport')
    )
    type = models.CharField(max_length=255, choices=type_choice, default='bullet')
    publisher = models.CharField(max_length=255)


