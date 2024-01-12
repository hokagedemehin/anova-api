from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

ROLE_CHOICES = (
    ('admin', 'Admin'),
    ('user', 'User'),
)

class NewUser(AbstractUser):
    email = models.EmailField(unique=True)
    role = models.CharField(choices=ROLE_CHOICES, max_length=10, default='user')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['-last_login']