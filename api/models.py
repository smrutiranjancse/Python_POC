from django.db import models

# Create your models here.

class Product(models.Model):
  name = models.CharField(max_length=30)
  price = models.IntegerField()
  ptype = models.CharField(max_length=20)
      
  def __str__(self):
    return self.title