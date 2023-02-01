# Generated by Django 4.1.5 on 2023-01-25 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_alter_place_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='img',
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='places.place')),
            ],
        ),
    ]