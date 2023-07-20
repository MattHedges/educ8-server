from django.db import models
from django.contrib.auth.models import User

class Library(models.Model):

    name = models.CharField(max_length=100),
    language = models.ForeignKey("Language", on_delete=models.CASCADE)
    summary = models.CharField(max_length=1000)