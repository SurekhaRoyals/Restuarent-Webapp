# Generated by Django 4.2.17 on 2024-12-25 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base_App', '0002_alter_items_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='Image',
            field=models.ImageField(blank=True, upload_to='Items/'),
        ),
        migrations.AlterField(
            model_name='items',
            name='Image',
            field=models.ImageField(upload_to='Items/'),
        ),
    ]
