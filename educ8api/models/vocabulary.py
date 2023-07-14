from django.db import models
from django.contrib.auth.models import User


class Vocabulary(models.Model):

    term = models.CharField(max_length=50)
    definition = models.CharField(max_length=500)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, null=True)
    example = models.CharField(max_length=1000, null=False)
    language = models.ForeignKey("Language", on_delete=models.CASCADE, null=False)