# Generated by Django 3.0.5 on 2020-12-23 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0048_auto_20201223_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttype',
            name='parent_product_type',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
    ]
