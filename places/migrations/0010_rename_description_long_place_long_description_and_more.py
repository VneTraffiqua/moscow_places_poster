# Generated by Django 4.1.5 on 2023-02-08 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0009_alter_photo_place'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='description_long',
            new_name='long_description',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='description_short',
            new_name='short_description',
        ),
    ]