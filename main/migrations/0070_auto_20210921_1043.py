# Generated by Django 3.0.5 on 2021-09-21 04:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0069_auto_20210921_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 21, 4, 43, 56, 67913, tzinfo=utc)),
        ),
    ]
