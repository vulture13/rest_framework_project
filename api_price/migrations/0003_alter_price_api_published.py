# Generated by Django 3.2.6 on 2022-09-16 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_price', '0002_alter_price_api_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price_api',
            name='published',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время'),
        ),
    ]