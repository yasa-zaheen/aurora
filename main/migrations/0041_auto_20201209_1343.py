# Generated by Django 3.0.5 on 2020-12-09 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0040_filter_background_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producttype',
            name='sub_category',
        ),
        migrations.DeleteModel(
            name='Filter',
        ),
        migrations.DeleteModel(
            name='ProductType',
        ),
    ]
