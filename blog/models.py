from django.db import models

# Create your models here.
class Post(models.Model):
    """Post model"""
    header = models.CharField(max_length=150, verbose_name='Author')
    text = models.TextField(verbose_name='Text')
    image = models.ImageField(upload_to='blog/', verbose_name='Image', null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='CreatedAt')
    published = models.BooleanField(default=True)
    views = models.IntegerField(default=0)
    class Meta:
        ordering = ['-created_at']
