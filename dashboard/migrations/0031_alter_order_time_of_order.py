# Generated by Django 3.2.8 on 2021-11-09 06:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0030_alter_order_time_of_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='time_of_order',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 9, 6, 58, 32, 776227, tzinfo=utc)),
        ),
    ]
