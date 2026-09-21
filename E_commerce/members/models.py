from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from datetime import timedelta
import random


class Brand(models.Model):
    brand = models.CharField(unique=True, max_length=200)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "brand"

    def __str__(self):
        return self.brand

# class Brand(models.Model):
#     brand = models.CharField(unique=True, max_length=200)
#     is_active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         db_table = "brand"
    
#     def __str__(self):
#         return f"({self.brand}), ({self.is_active}), ({self.created_at}), ({self.updated_at})"


class Product(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    product_name = models.CharField(unique=True, max_length=200)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "product"
    
    # def __str__(self):
    #     return f"({self.brand.brand}, {self.product_name}), ({self.is_active}), ({self.created_at}), ({self.updated_at})"

    def __str__(self):
        return self.product_name


class Sub_Category(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category_name = models.CharField(unique=True, max_length=200)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "sub_category"
    
    # def __str__(self):
    #     return f"({self.product.product_name}), ({self.brand.product_name}), ({self.category_name}), ({self.price}), ({self.created_at}), ({self.updated_at})"

    def __str__(self):
        return f"{self.product.product_name} - {self.brand.brand_name} - {self.category_name}"