from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = "core"
urlpatterns = [
    # Url dirigida al índice base
    path('', views.indice, name="indice"),

    # Urls dirigidas a la información básica de la web "Conocer"
    path('introduccion/', views.introduccion, name="introduccion"),
    path('amigos/', views.amigos, name="amigos"),
    path('despedidaSoltero/', views.despedidaSoltero, name="despedidaSoltero"),
    path('compañerosTrabajo/', views.compañerosTrabajo, name="compañerosTrabajo"),
    path('familia/', views.familia, name="familia"),

    # Urls dirigidas a la información del usuario "Perfil"
    path('indexUsuario/', views.indexUsuario, name="indexUsuario"),
    path('perfil/', views.perfil, name="perfil"),
    path('actualizar/', views.actualizarUsuario, name='actualizarUsuario'),
    path('cambiarContrasena/', views.cambiarContrasena, name='cambiarContrasena'),
    path('bonosComprados/', views.bonosComprados, name="bonosComprados"),
    path('darDeBaja/', views.darDeBaja, name='darDeBaja'),

    # Url dirigida a la información de los bonos "Bonos"
    path('bonos/', views.bonos, name="bonos"),

    # Url dirigida a la información de la programación semanal "ProgramacionSemanal"
    path('programacion/', views.programacionSemanal, name="programacionSemanal"),

    # Urls dirigidas al acceso del usuario "AccesoUsuario"
    path('login/', views.iniciarSesion, name="login"),
    path('exit/', views.exit, name='exit'),
    path('registro/', views.registrarUsuario, name='register'),

    # Urls dirigidas a la información de las salas y su reserva "Salas"
    path('salas/', views.listaSalas, name='listaSalas'),
    path('tipoSalas/', views.tipoSalas, name='tipoSalas'),
    path('reservar/<int:horario_id>/', views.reservarSala, name='reservarSala'),
    path('salasReservadas/', views.salasReservadas, name='salasReservadas'),

    # Añade una ruta adicional a urlpatterns para servir archivos de medios
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)       # URL base y directorio del sistema de archivos donde se almacenan los archivos de medios