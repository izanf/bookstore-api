from django.db import models

# Create your models here.
class BookModel(models.Model):
  title: models.CharField(max_length=255)
  isBn: models.CharField()
  isBn13: models.CharField(max_length=13)
  languageCode: models.CharField(max_length=3)
  numPages: models.IntegerField()
  publicationDate: models.DateField()
  author: models.ForeignKey('AuthorModel', on_delete=models.DO_NOTHING)
  publisher: models.ForeignKey('PublisherModel', on_delete=models.DO_NOTHING)

class AuthorModel(models.Model):
  first_name: models.CharField(max_length=255)
  last_name: models.CharField(max_length=255)

class PublisherModel(models.Model):
  name: models.CharField(max_length=255)