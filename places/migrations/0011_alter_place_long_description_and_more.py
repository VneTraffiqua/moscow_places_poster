# Generated by Django 4.1.5 on 2023-02-08 09:35

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0010_rename_description_long_place_long_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='long_description',
            field=tinymce.models.HTMLField(blank=True, help_text='Введите описание', null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='short_description',
            field=models.CharField(blank=True, help_text='Введите короткое описание', max_length=255, null=True, verbose_name='Короткое описание'),
        ),
    ]
