# Generated by Django 3.0.5 on 2021-09-21 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0073_product_price_last_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock_last_updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
