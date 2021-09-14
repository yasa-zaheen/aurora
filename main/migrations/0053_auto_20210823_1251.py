# Generated by Django 3.0.5 on 2021-08-23 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0052_auto_20210823_1248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='sub_category',
        ),
        migrations.AddField(
            model_name='product',
            name='sub_category',
            field=models.ForeignKey(limit_choices_to={'category': models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Category')}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.SubCategory'),
        ),
    ]
