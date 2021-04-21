from django.db import models


class Photo(models.Model):
    picture = models.ImageField()
