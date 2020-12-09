from django.db import models
from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError
import mimetypes
import os
# Create your models here.


class Status(models.Model):
    title=models.CharField(max_length=200, null=True )
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

def validate_image(image):
    file_size = image.file.size
    limit_mb = 2
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError("Max size of file is %s KB" % limit_mb)

def validate_file(file):
    ext = os.path.splitext(file.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf','.doc', '.docx', '.jpg', '.png', '.ppt', '.pptx', '.text']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Please choose these  %s file type' % valid_extensions)
    file_size = file.file.size
    limit_mb = 250
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError("Max size of file is %s KB" % limit_mb)

class Visitorbook(models.Model):
    purpose=models.CharField(max_length=200, null=True )
    name=models.CharField(max_length=200, null=True )
    phone=models.CharField(max_length=200, null=True )
    id_card=models.CharField(max_length=200, null=True )
    date=models.DateField(null=True, blank=True)
    in_time=models.TimeField(null=True, blank=True)
    out_time=models.TimeField(null=True, blank=True)
    note=models.TextField(null=True,blank=True)
    attachment=models.FileField(upload_to='visitorbook', null=True, blank=True,validators=[validate_file])
    image=models.ImageField(upload_to='visitorbook' null=True, validators=[validate_image])
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title