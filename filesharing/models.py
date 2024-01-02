from django.db import models

# Create your models here.


class UploadFile(models.Model):
    filename = models.CharField(max_length=255)
    size = models.PositiveIntegerField()
    file_type = models.CharField(max_length=50)
    file = models.FileField()
