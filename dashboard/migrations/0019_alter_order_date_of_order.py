# Generated by Django 3.2.8 on 2021-11-01 05:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0018_auto_20210930_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_of_order',
            field=models.DateField(default=datetime.datetime(2021, 11, 1, 5, 38, 46, 133623, tzinfo=utc)),
        ),
    ]
