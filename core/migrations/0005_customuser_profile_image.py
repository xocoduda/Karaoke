# Generated by Django 5.0.4 on 2024-05-14 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_bonoregalo_email_receptor'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profile_image',
            field=models.ImageField(default='profile_images/default.png', upload_to='profile_images/'),
        ),
    ]