from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField('Name', max_length=50)
    description = models.TextField('Description')