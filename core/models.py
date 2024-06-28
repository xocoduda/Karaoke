from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    profile_images = models.ImageField(upload_to='profile_images/', default='profile_images/default.png', null=True, blank=True)

    def __str__(self):
        return self.email

class Saladekaraoke(models.Model):
    id_sala = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    disponibilidad = models.BooleanField()

    class Meta:
        db_table = 'saladekaraoke'
        verbose_name = "Sala"
        verbose_name_plural = "Salas"

    def __str__(self):
        return self.nombre

class HorarioSala(models.Model):
    sala = models.ForeignKey(Saladekaraoke, on_delete=models.CASCADE)
    dia = models.CharField(max_length=20, default='Miércoles')
    inicio = models.TimeField()
    fin = models.TimeField()
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0);

    class Meta:
        db_table = 'horario_sala'
        verbose_name = "Horario"
        verbose_name_plural = "Horarios"
    
    def __str__(self):
        return f"{self.sala.nombre} ({self.inicio} - {self.fin})"

class Reserva(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    sala = models.ForeignKey(Saladekaraoke, on_delete=models.CASCADE)
    horario = models.ForeignKey(HorarioSala, on_delete=models.CASCADE, null=True, blank=True)
    estado = models.CharField(max_length=20, default='Reservado')

    class Meta:
        db_table = 'reserva'
        unique_together = ('sala', 'horario')
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"

class Bonoregalo(models.Model):
    id_bono = models.AutoField(primary_key=True)
    emisor = models.ForeignKey(CustomUser, related_name='bonos_emitidos', on_delete=models.CASCADE)
    nombre_receptor = models.CharField(max_length=100, null=True)
    apellidos_receptor = models.CharField(max_length=100, null=True)
    valor = models.PositiveIntegerField(choices=[(50, '50 €'), (80, '80 €'), (100, '100 €')], default=50)
    mensaje = models.TextField()

    class Meta:
        db_table = 'bonoregalo'
        verbose_name = "Bono"
        verbose_name_plural = "Bonos"