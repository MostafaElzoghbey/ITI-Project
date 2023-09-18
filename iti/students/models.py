from django.db import models
from authmansoura.models import *

# Create your models here.


class books(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=80)
    photo = models.ImageField(upload_to='static/images')

    def __str__(self):
        return self.title


class borrowbook(models.Model):
    account = models.ForeignKey(
        Myaccount, null=True, on_delete=models.SET_NULL)
    borrbook = models.ForeignKey(books, null=True, on_delete=models.SET_NULL)
    id = models.AutoField(primary_key=True)
