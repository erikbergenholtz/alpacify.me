from django.db import models

# Create your models here.

class Image(models.Model):
    image_b64 = models.CharField(max_length=682668)
    image_hash = models.CharField(max_length=32)
