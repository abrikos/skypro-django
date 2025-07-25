from django.contrib import admin
from django.contrib.auth import get_user_model

# Register your models here.
from .models import Product, Category, Contacts

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','category')
    list_filter = ('category',)
    search_fields = ('name', 'desc')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','desc')
    search_fields = ('name', 'desc')

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id','email','phone')


admin.site.register(get_user_model())