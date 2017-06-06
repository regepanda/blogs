from django.db import models

# Create your models here.
class Article(models.Model):
    article_name = models.CharField(max_length=100)
    article_title = models.CharField(max_length=200)
    article_content = models.TextField()
    author_name = models.CharField(max_length=100)
    author_occupation = models.CharField(max_length=100)
