from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Category Model.

class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    # Delete comments if product is deleted
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="reviews"
        )
    name = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_post")
    body = models.TextField()
    created_on = models.DateTimeField(
        auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.product.name, self.name)
    
    def get_absolute_url(self):
        return reverse('products')


