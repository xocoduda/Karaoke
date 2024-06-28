from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .models import Bonoregalo, Saladekaraoke, HorarioSala, Reserva
from .forms import CustomUserCreationForm, EmailAuthenticationForm, BonoregaloForm, CustomUserChangeForm

# Vistas de comportamiento básico
def indice(request):
    return render(request, "index.html")

def introduccion(request):
    return render(request, "Conocer/introduccion.html")

def tipoSalas(request):
    return render(request, "Salas/explicacionSalas.html")

def amigos(request):
    return render(request, "Conocer/amigos.html")

def despedidaSoltero(request):
    return render(request, "Conocer/despedidaSoltero.html")

def compañerosTrabajo(request):
    return render(request, "Conocer/compañerosTrabajo.html")

def familia(request):
    return render(request, "Conocer/familia.html")

def programacionSemanal(request):
    return render(request, "ProgramacionSemanal/programacionSemanal.html")

def indexUsuario(request):
    return render(request, "Perfil/indexUsuario.html")

# Vista para mostrar la lista de salas y sus horarios según el día seleccionado
def listaSalas(request):
    salas = Saladekaraoke.objects.all().order_by('capacidad')
    dia_seleccionado = request.GET.get('dia', 'Miércoles')      # Se obtiene el valor del parámetro 'dia' de la solicitud GET, si no se proporciona, se establece por defecto en 'Miércoles'
    dias_disponibles = ['Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    horarios = HorarioSala.objects.filter(dia=dia_seleccionado)
    horarios_info = []
    for horario in horarios:
        is_reserved = Reserva.objects.filter(horario=horario).exists()        # Se verifica si hay una reserva para el horario actual
        horarios_info.append((horario, is_reserved))        # Se agrega la información del horario y su disponibilidad a la lista
    
    contexto = {
        'salas': salas,
        'horarios_info': horarios_info,
        'dias_disponibles': dias_disponibles,
        'dia_seleccionado': dia_seleccionado,
    }
    return render(request, 'Salas/listaSalas.html', contexto)

# Vista para manejar la reserva de una sala
def reservarSala(request, horario_id):
    horario = HorarioSala.objects.get(id=horario_id)

    if Reserva.objects.filter(horario=horario).exists():
        messages.error(request, 'La sala no está disponible en el horario seleccionado.')
    else:
        Reserva.objects.create(     # Si la sala está disponible, crea una nueva reserva
            usuario=request.user,
            sala=horario.sala,
            horario=horario,
            estado='Reservado'
        )
        messages.success(request, '¡Sala reservada con éxito!')
    return redirect('core:listaSalas')

# Vista para mostrar las salas reservadas por el usuario
def salasReservadas(request):
    usuario = request.user
    reservas = Reserva.objects.filter(usuario=usuario).select_related('sala', 'horario')    # Filtra las salas reservadas por el usuario mostrando los campos de sala y horario reservados
    return render(request, 'Perfil/salasReservadas.html', {'reservas': reservas})

# Vista para mostrar el perfil del usuario
def perfil(request):
    usuario = request.user
    bonos = Bonoregalo.objects.filter(emisor=usuario)
    salas = Reserva.objects.filter(usuario=request.user).select_related('sala', 'horario')
    return render(request, 'Perfil/perfil.html', {'usuario': usuario, 'bonos': bonos, 'salas': salas})

# Vista para manejar la compra de bonos
def bonos(request):
    if request.method == 'POST':
        form = BonoregaloForm(request.POST)
        if form.is_valid():
            bono = form.save(commit=False)     # Si el formulario es válido, guarda la instancia del formulario en la base de datos pero no la confirma
            bono.emisor = request.user
            bono.save()
            return redirect('core:indice')
    else:
        form = BonoregaloForm()
    return render(request, "Bonos/bonos.html", {'form': form, 'user': request.user})

# Vista para mostrar los bonos comprados por el usuario
def bonosComprados(request):
    usuario = request.user
    bonos = Bonoregalo.objects.filter(emisor=usuario)
    return render(request, 'Perfil/bonosComprados.html', {'usuario': usuario, 'bonos': bonos})

# Vista para manejar el inicio de sesión
def iniciarSesion(request):
    if request.method == 'POST':
        form = EmailAuthenticationForm(request=request, data=request.POST)  # Crea una instancia del formulario de autenticación con los datos enviados
        if form.is_valid():
            user = form.get_user()  # Obtiene el usuario autenticado del formulario
            login(request, user, backend='core.backends.EmailBackend')  # Autentica al usuario usando el backend personalizado
            return redirect('core:indice')
        else:
            messages.error(request, 'Credenciales incorrectas. Por favor, inténtalo de nuevo.')
    else:
        form = EmailAuthenticationForm()  # Crea una instancia vacía del formulario si el método no es POST
    return render(request, 'AccesoUsuario/login.html', {'form': form}) 

# Vista para manejar el registro de un nuevo usuario
def registrarUsuario(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')  # Autentica al usuario recién registrado
            return redirect('core:indice') 
    else:
        form = CustomUserCreationForm()
    return render(request, 'AccesoUsuario/register.html', {'form': form}) 

# Vista para manejar la eliminación de la cuenta del usuario
def darDeBaja(request):
    if request.method == 'POST':
        user = request.user
        if user.is_authenticated:
            user.delete()
            messages.success(request, 'Tu cuenta ha sido eliminada.')
            return redirect('core:indice')
        else:
            return redirect('core:indice')
    return render(request, 'core/indice.html', {'alert_message': 'Tu cuenta ha sido eliminada.'}) 

# Vista para manejar el cierre de sesión del usuario
def exit(request):
    logout(request)
    return redirect('core:indice')

# Vista para manejar la actualización del perfil del usuario
def actualizarUsuario(request):
    if request.method == 'POST':  
        formularioUsuario = CustomUserChangeForm(request.POST, instance=request.user)  
        if formularioUsuario.is_valid():  
            user = formularioUsuario.save(commit=False)
            if 'email' in formularioUsuario.changed_data:  # Comprueba si el email ha cambiado
                user.email = formularioUsuario.cleaned_data['email']  # Actualiza el email del usuario
            if 'username' in formularioUsuario.changed_data:  
                user.username = formularioUsuario.cleaned_data['username'] 
            user.save() 
            messages.success(request, '¡Datos de usuario actualizados correctamente!')
            return redirect('core:perfil')  
        else:
            messages.error(request, 'Por favor corrija los errores a continuación.')  
    else:
        formularioUsuario = CustomUserChangeForm(instance=request.user)
    
    return render(request, 'Perfil/actualizar.html', {  
        'formularioUsuario': formularioUsuario,
        'formularioContrasenna': PasswordChangeForm(request.user)
    })

# Vista para manejar la actualización de contraseña del usuario
def cambiarContrasena(request): 
    if request.method == 'POST':
        formularioContrasenna = PasswordChangeForm(request.user, request.POST)  # Crea una instancia del formulario de cambio de contraseña con los datos enviados y la instancia del usuario actual
        if formularioContrasenna.is_valid():
            user = formularioContrasenna.save() 
            update_session_auth_hash(request, user)  # Actualiza la sesión con la nueva contraseña
            messages.success(request, '¡Contraseña cambiada correctamente!') 
            return redirect('core:perfil') 
        else:
            messages.error(request, 'Por favor corrija los errores a continuación.')
    else:
        formularioContrasenna = PasswordChangeForm(request.user)  # Crea una instancia vacía del formulario si el método no es POST

    return render(request, 'Perfil/actualizar.html', { 
        'formularioUsuario': CustomUserChangeForm(instance=request.user),
        'formularioContrasenna': formularioContrasenna
    })