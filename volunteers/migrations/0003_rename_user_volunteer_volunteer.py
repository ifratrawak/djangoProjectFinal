# Generated by Django 4.1.4 on 2023-10-25 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0002_volunteer_store_alter_volunteer_user_delete_webuser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='volunteer',
            old_name='user',
            new_name='volunteer',
        ),
    ]
