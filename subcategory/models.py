from django.db import models
from category.models import Category


# Create your models here.
class SubCategory(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="subcategories"
    )
    sub_cat_name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to="subcategory_icons/")
