from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import mimetypes
import os

# Create your models here.

class Author(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField(max_length=200, null=True, blank=True)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 

