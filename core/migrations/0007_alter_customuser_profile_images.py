# Generated by Django 5.0.4 on 2024-05-14 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_customuser_profile_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_images',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]