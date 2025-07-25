from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    email = models.EmailField(verbose_name='почта', unique=True)
    avatar = models.ImageField(upload_to='users/', verbose_name='AvatarImage', null=True)
    phone = models.CharField(max_length=15, verbose_name='Phone', null=True)
    country = models.CharField(max_length=50, verbose_name='Country', null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []