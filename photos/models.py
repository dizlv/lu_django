from django.db import models
from django.conf import settings


class Photo(models.Model):
    picture = models.ImageField(upload_to='photos')
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
