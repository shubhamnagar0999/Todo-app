from distutils.text_file import TextFile
from email.policy import default
from django.db import models

# Create your models here.
class tasks(models.Model):
    task = models.TextField(default=None)