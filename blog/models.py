from django.db import models
from django.urls import reverse

# Create your models here.

class Article(models.Model):
    author      = models.CharField(max_length=100)
    title       = models.CharField(max_length=120)
    description = models.TextField(blank=True,null=True)
    body        = models.TextField(max_length=True)
    summary     = models.TextField(default="This is cool")

    def get_absolute_url(self):
        return reverse('blog:article_detail',kwargs= {"id": self.id})                              #f"/articles/{self.id}"
