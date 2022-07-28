from django.db import models

# Create your models here.
class Product(models.Model):
    name= models.CharField(max_length=10)
    details= models.TextField()
    price= models.PositiveIntegerField()
    image= models.ImageField(upload_to='pics')
    update= models.DateTimeField(auto_now=True)