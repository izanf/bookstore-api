from django.db import models

class Books(models.Model):
  title = models.CharField(max_length=255)
  is_bn = models.CharField(max_length=10)
  is_bn_13 = models.CharField(max_length=13)
  language_code = models.CharField(max_length=3)
  num_pages = models.IntegerField(null=False)
  average_rating = models.IntegerField(default=1)
  ratings_count = models.IntegerField(default=0)
  text_reviews_count = models.IntegerField(default=0)
  publication_date = models.DateField(auto_now_add=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True, null=True)
  publisher = models.ForeignKey('Publishers', on_delete=models.DO_NOTHING, null=True)
  author = models.ForeignKey('Authors', on_delete=models.DO_NOTHING, null=True)

class Authors(models.Model):
  name = models.CharField(max_length=45, unique=True)

class Publishers(models.Model):
  name = models.CharField(max_length=255)