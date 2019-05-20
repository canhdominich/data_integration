from django.db import models

# Create your models here.
class NewsPaper(models.Model):
    time = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    category = models.IntegerField()
    thumbnail = models.CharField(max_length=250)
    description = models.TextField()
    content = models.TextField()
    author = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "newspaper"