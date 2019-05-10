# Generated by Django 2.2.1 on 2019-05-09 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254, verbose_name='Email Address')),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
