from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    language = models.ForeignKey("Language", on_delete=models.CASCADE)