from django.db import models

# Create your models here.
class Contacts(models.Model):
    email = models.CharField(max_length=150, verbose_name='Email')
    phone = models.CharField(max_length=150, verbose_name='Phone')

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Name')
    desc = models.CharField(max_length=150, verbose_name='Description')
    def __str__(self):
        return f'{self.name} {self.desc}'


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Name')
    desc = models.CharField(max_length=150, verbose_name='Description')
    image = models.ImageField(upload_to='images/', verbose_name='Image')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.FloatField(max_length=150, verbose_name='Price')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='CreatedAt')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='UpdatedAt')

    def __str__(self):
        return f'{self.name} {self.desc} {self.price}'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['created_at']

