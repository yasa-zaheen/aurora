# Generated by Django 3.0.5 on 2021-09-25 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0075_auto_20210925_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='last_updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
