# Generated by Django 3.2 on 2022-06-05 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20220605_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='likes',
            field=models.IntegerField(blank=True, default='0', null=True),
        ),
    ]