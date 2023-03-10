# Generated by Django 4.1.5 on 2023-02-07 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_alter_place_lat_alter_place_lon_alter_place_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='number',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(unique=True, upload_to='media/', verbose_name='Изображение'),
        ),
    ]
