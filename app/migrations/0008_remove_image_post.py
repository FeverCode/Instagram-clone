# Generated by Django 3.2 on 2022-06-05 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_image_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='post',
        ),
    ]