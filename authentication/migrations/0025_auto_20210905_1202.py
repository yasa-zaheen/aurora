# Generated by Django 3.0.5 on 2021-09-05 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0024_customuser_cover_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='customuser',
            name='contact',
            field=models.CharField(default='', max_length=255),
        ),
    ]
