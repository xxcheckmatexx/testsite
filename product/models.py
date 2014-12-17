from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Product(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField()
  slug = models.SlugField(null=True)
  image = models.ImageField(upload_to='static')


  def save(self, *args, **kwargs):
    if not self.id:
      self.slug = slugify(self.title)
    super(Product, self).save(*args, **kwargs)

  def __str__(self):
    return self.title