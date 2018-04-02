from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Film(models.Model):
    name = models.CharField(verbose_name='电影名',max_length=20)
    brief = models.TextField(verbose_name="电影介绍")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '电影'
        verbose_name_plural = verbose_name