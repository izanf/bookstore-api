from django.db import models

# Create your models here.
class Books(models.Model):
  title = models.CharField(max_length=45)
  isBn = models.CharField(max_length=8)
  isBn13 = models.CharField(max_length=13)
  languageCode = models.CharField(max_length=3)
  numPages = models.IntegerField()
  publicationDate = models.DateField(auto_now_add=True)
  created_at = models.DateTimeField(auto_now_add=True)

class Authors(models.Model):
  first_name = models.CharField(max_length=45)
  last_name = models.CharField(max_length=45)

class Publishers(models.Model):
  name = models.CharField(max_length=45)