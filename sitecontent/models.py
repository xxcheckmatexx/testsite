from django.db import models

# Create your models here.
class Content(models.Model):
  title = models.CharField(max_length=200)
  content = models.TextField(max_length=1000)
  slug = models.SlugField(max_length=40)