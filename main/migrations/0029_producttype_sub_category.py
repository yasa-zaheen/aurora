# Generated by Django 3.0.5 on 2020-11-02 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_remove_producttype_year_in_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttype',
            name='sub_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.SubCategory'),
        ),
    ]
