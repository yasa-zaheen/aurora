# Generated by Django 3.0.5 on 2021-08-29 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0021_customuser_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='cover_image',
            field=models.ImageField(default='cover_images/cover.jpg', upload_to='cover_images'),
        ),
    ]
