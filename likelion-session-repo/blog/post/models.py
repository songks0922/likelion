from django.db import models
from django.conf import settings
# Create your models here.


class Post(models.Model):
    content = models.CharField(max_length=150)
    user = models.CharField(max_length=30)
