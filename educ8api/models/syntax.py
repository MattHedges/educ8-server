from django.db import models
from django.contrib.auth.models import User


class Syntax(models.Model):

    language = models.ForeignKey("Language", on_delete=models.CASCADE)
    question = models.ForeignKey("Question", on_delete=models.CASCADE)
    answer = models.ForeignKey("Question", on_delete=models.CASCADE, related_name="answer")
    category = models.ForeignKey("Category", on_delete=models.CASCADE)