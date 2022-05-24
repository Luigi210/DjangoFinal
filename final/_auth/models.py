from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.



class User(AbstractUser):
    SUPER_ADMIN = 1
    GUEST = 2

    ROLE_CHOICES = (
        (SUPER_ADMIN, 'Super Admin'),
        (GUEST, 'Guest')
    )

    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)


    