from django.db import models

class Price_api(models.Model):
    title = models.CharField(max_length=255, blank=True, verbose_name='Название')
    content = models.TextField(blank=True, verbose_name='Описание')
    published = models.DateTimeField(auto_now_add=False, verbose_name='Время')

    class Meta:
        ordering = ['-published']

    def __str__(self):
        return self.title    