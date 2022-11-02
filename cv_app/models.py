from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class CvModel(models.Model):
    file_name = models.CharField(max_length=25)
    my_file = models.FileField()