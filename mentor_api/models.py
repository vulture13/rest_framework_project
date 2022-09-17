from django.db import models

class Mentor(models.Model):
    name = models.CharField(max_length=255, verbose_name='ФИО')
    content = models.TextField(verbose_name='Описание')
    img = models.ImageField(upload_to='media/', blank=True)

    def __str__(self):
        return self.name
