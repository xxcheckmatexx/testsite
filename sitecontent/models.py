from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Content(models.Model):
  title = models.CharField(max_length=200)
  content = models.TextField()
  slug = models.SlugField(null=True, blank=True)
  def save(self, *args, **kwargs):
    if not self.id:
      self.slug = slugify(self.title)
    super(Content, self).save(*args, **kwargs)

  def __str__(self):
        return self.title