# Generated by Django 3.0.5 on 2020-12-15 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0043_auto_20201214_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttype',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
