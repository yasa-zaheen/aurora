# Generated by Django 3.2.8 on 2021-10-12 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0078_auto_20211012_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='old_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='old_stock',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
