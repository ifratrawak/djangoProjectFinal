# Generated by Django 4.2.6 on 2023-10-18 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='photo',
        ),
    ]
