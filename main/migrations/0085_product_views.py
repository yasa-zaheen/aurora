# Generated by Django 3.2.8 on 2021-11-09 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0084_auto_20211108_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
