from django.db import models

class Images_api(models.Model):
    img = models.ImageField(null=True, blank=True, upload_to="media/", verbose_name='Изображение')

    
