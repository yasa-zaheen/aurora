# Generated by Django 3.0.5 on 2020-11-04 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_auto_20201104_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttype',
            name='image_photographer_url',
            field=models.URLField(blank=True),
        ),
    ]
