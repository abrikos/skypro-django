from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

class Manager(UserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Пользователь должен иметь email')
        user=self.model(email=email,)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, password=None):
        user=self.model(email=email,)
        user.username=""
        user.is_staff=True
        user.is_superuser=True
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractUser):
    objects = Manager()
    username = None
    email = models.EmailField(verbose_name='почта', unique=True)
    avatar = models.ImageField(upload_to='users/', verbose_name='AvatarImage', null=True)
    phone = models.CharField(max_length=15, verbose_name='Phone', null=True)
    country = models.CharField(max_length=50, verbose_name='Country', null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email