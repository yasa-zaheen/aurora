# Generated by Django 3.2.8 on 2021-11-09 07:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0034_alter_order_time_of_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='time_of_order',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 9, 7, 0, 54, 717434, tzinfo=utc)),
        ),
    ]
