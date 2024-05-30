from django.db import models

# Create your models here.

class RecipeModel(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    desc = models.CharField(max_length=350)
    