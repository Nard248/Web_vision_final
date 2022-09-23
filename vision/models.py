from django.db import models


class Image(models.Model):
    search_word = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Uploads')
