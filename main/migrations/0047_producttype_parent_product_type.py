# Generated by Django 3.0.5 on 2020-12-23 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0046_auto_20201215_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttype',
            name='parent_product_type',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
