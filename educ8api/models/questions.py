from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):

    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=1000)
    example = models.CharField(max_length=1000)
    language = models.ForeignKey("Language", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)