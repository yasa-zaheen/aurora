# Generated by Django 3.2.8 on 2021-11-09 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0100_alter_product_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='views',
        ),
    ]
