# Generated by Django 4.2.5 on 2023-09-21 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bear',
            name='weight_bottom',
            field=models.IntegerField(blank=True),
        ),
    ]