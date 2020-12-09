from django.db import models

# Create your models here.
class Destination(models.Model):

    name=models.CharField( max_length=50)
    images=models.ImageField(upload_to='images')
    description=models.TextField()
    price=models.FloatField()
    offer=models.BooleanField(default=False)

class Test(models.Model):
    name=models.CharField(max_length=100)