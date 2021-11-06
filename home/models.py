from django.db import models

# Create your models here.
class Images(models.Model):
    image_id = models.IntegerField(primary_key=True)
    image_name = models.IntegerField()
    description = models.TextField()
    microscopy = models.CharField(max_length=400)
    cell_type = models.CharField(max_length=300)
    component = models.CharField(max_length=150)
    doi = models.CharField(max_length=450)
    organism = models.CharField(max_length=500)

"""class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=50)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
"""

