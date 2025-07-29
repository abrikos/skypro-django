from django.db import models

from my_site import settings
from users.models import User


# Create your models here.
class Contacts(models.Model):
    """Contacts model"""
    email = models.CharField(max_length=150, verbose_name='Email')
    phone = models.CharField(max_length=150, verbose_name='Phone')

class Category(models.Model):
    """Category model"""
    name = models.CharField(max_length=150, verbose_name='Name')
    desc = models.CharField(max_length=150, verbose_name='Description')
    def __str__(self):
        return f'{self.name} {self.desc}'


class Product(models.Model):
    """Product model"""
    name = models.CharField(max_length=150, verbose_name='Name')
    desc = models.TextField(max_length=150, verbose_name='Description')
    image = models.ImageField(upload_to='images/', verbose_name='Image')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='Owner', null=True)
    price = models.FloatField(max_length=150, verbose_name='Price')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='CreatedAt')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='UpdatedAt')
    published = models.BooleanField(default=False, verbose_name='Published')

    def __str__(self):
        return f'{self.name} {self.desc} {self.price}'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['created_at']
        permissions = [
            ("can_publish_product", "Can publish product"),
            ("can_unpublish_product", "Can unpublish product"),
            ("can_delete_product", "Can delete product"),
        ]

