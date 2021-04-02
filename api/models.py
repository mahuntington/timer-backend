from django.db import models

# Create your models here.
class Session(models.Model):
    seconds = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

