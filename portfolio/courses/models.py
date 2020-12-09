from django.db import models

# Create your models here.
class Course(models.Model):
    images=models.ImageField(upload_to='images')
    summary=models.CharField( max_length=200)

    def __str__(self):
        return self.summary

    def delete(self, *args, **kwargs):
        self.images.delete()
        super().delete(*args, **kwargs)
    