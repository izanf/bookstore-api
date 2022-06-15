from django.db import models

class Books(models.Model):
  title = models.CharField(max_length=255)
  subtitle = models.CharField(max_length=255, null=True)
  description = models.TextField(max_length=5000)
  is_bn = models.CharField(max_length=10)
  is_bn_13 = models.CharField(max_length=13)
  language = models.CharField(max_length=3)
  info_link = models.CharField(max_length=100)
  image = models.CharField(max_length=255)
  categories = models.CharField(max_length=100)
  maturity_rating = models.CharField(max_length=10)
  page_count = models.IntegerField(null=False)
  authors = models.CharField(max_length=100)
  publisher = models.CharField(max_length=100)
  published_date = models.DateField(null=True)
  created_at = models.DateTimeField(auto_now_add=True, null=True)
  # publisher = models.ForeignKey('Publishers', on_delete=models.DO_NOTHING, null=True)
  # author = models.ForeignKey('Authors', on_delete=models.DO_NOTHING, null=True)

  # class Authors(models.Model):
  #   name = models.CharField(max_length=45, unique=True)

  # class Publishers(models.Model):
  # name = models.CharField(max_length=255)