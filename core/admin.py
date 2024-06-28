from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Bonoregalo, Saladekaraoke, HorarioSala, Reserva
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Configuración de la vista en línea para Bonoregalo
class BonoregaloInline(admin.TabularInline):
    model = Bonoregalo
    extra = 0
    fields = ('id_bono', 'nombre_receptor', 'apellidos_receptor', 'valor', 'mensaje')
    readonly_fields = ('id_bono', 'nombre_receptor', 'apellidos_receptor', 'valor', 'mensaje')

# Configuración del modelo Bonoregalo en el admin
@admin.register(Bonoregalo)
class BonoregaloAdmin(admin.ModelAdmin):
    list_display = ('id_bono', 'emisor', 'nombre_receptor', 'apellidos_receptor', 'valor', 'mensaje')
    list_filter = ('emisor', 'valor')
    search_fields = ('emisor__email', 'nombre_receptor', 'apellidos_receptor')

# Configuración del modelo CustomUser en el admin
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'date_joined', 'profile_images']
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'profile_images')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active', 'is_staff', 'profile_images')}
        ),
    )
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)

class HorarioSalaInline(admin.TabularInline):
    model = HorarioSala
    extra = 1

class ReservaInline(admin.TabularInline):
    model = Reserva
    extra = 1

class SaladekaraokeAdmin(admin.ModelAdmin):
    inlines = [HorarioSalaInline, ReservaInline]
    list_display = ('nombre', 'capacidad')
    search_fields = ('nombre',)

class HorarioSalaAdmin(admin.ModelAdmin):
    list_display = ('sala', 'dia', 'inicio', 'fin', 'precio')
    list_filter = ('sala',)

class ReservaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'sala', 'horario', 'estado')
    list_filter = ('sala', 'estado')
    search_fields = ('usuario__email', 'sala__nombre')

admin.site.register(Saladekaraoke, SaladekaraokeAdmin)
admin.site.register(HorarioSala, HorarioSalaAdmin)
admin.site.register(Reserva, ReservaAdmin)