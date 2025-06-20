from django.contrib import admin

# Register your models here.
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','header','text','image')
    search_fields = ('header', 'text')

