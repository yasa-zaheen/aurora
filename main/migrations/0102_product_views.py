# Generated by Django 3.2.8 on 2021-11-09 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0101_remove_product_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='views',
            field=models.JSONField(default=[]),
        ),
    ]
