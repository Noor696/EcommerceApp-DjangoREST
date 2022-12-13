from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class School(models.Model):
    owner = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    rate = models.IntegerField()
    img_url = models.TextField(default="no image provided")

    def __str__(self):
        return self.name