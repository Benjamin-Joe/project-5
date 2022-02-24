"Admin.py In Store App"
from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    "Class to display category properties"
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    "Class to display product properties"
    list_display = ['title', 'slug', 'price', 'created_on']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['price', ]
