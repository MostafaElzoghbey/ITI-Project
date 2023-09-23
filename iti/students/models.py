from django.db import models
from authmansoura.models import *

# Create your models here.


class books(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=80)
    photo = models.ImageField(upload_to='static/images')
    available = models.BooleanField(default=True)
    def __str__(self):
        return self.title


# class borrowbook(models.Model):
#     account = models.ForeignKey(
#         Myaccount, null=True, on_delete=models.SET_NULL)
#     borrbook = models.ForeignKey(books, null=True, on_delete=models.SET_NULL)
#     id = models.AutoField(primary_key=True)

class borrowbook(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Myaccount, on_delete=models.CASCADE)
    book = models.ForeignKey(books, on_delete=models.CASCADE)
    borrowed_date = models.DateField()
    due_date = models.DateField()

    def __str__(self):
        return f"Book {self.book.title} borrowed by {self.student.username}"