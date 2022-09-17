from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Request_api(models.Model):
    name = models.CharField(max_length=256, verbose_name='ФИО')
    number_phone = PhoneNumberField(blank=True, verbose_name='Номер телефона')
    published = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.name
