"Main Models File"
from django.db import models


class Category(models.Model):
    "Category creation model"
    name = models.CharField(max_length=100, unique=True, db_index=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        "Returns category name"
        return self.name

    class Meta:
        "Changes name in admin section"
        verbose_name_plural = 'Categories'


class Product(models.Model):
    "Product creation model"
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(blank=True, null=True, max_digits=6,
                                 decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        "Class to display newest products first"
        ordering = ('-created_on',)

    def __str__(self):
        "Return product title"
        return self.title
