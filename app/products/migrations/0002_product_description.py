# Generated by Django 2.2.1 on 2019-05-08 10:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default=django.utils.timezone.now, verbose_name='Awesome'),
            preserve_default=False,
        ),
    ]
