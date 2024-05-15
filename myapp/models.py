from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=25)
    age=models.IntegerField()


class Book(models.Model):
    bookName=models.CharField(max_length=30)
    price=models.FloatField()
    author=models.ForeignKey(Author,on_delete=models.CASCADE)

