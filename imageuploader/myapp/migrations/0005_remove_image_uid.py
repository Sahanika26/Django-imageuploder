# Generated by Django 5.0.1 on 2024-01-18 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_image_uid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='uid',
        ),
    ]
