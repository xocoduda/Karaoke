# Generated by Django 5.0.4 on 2024-06-03 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_reserva_estado_horariosala_reserva_horario_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='horariosala',
            name='dia',
            field=models.CharField(default='Lunes', max_length=20),
        ),
    ]
