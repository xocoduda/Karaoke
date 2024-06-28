from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser, Bonoregalo
from django.contrib.auth import authenticate

# Define un formulario de creación de usuario personalizado heredando de UserCreationForm
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta): 
        model = CustomUser
        fields = ('email', 'username', 'password1', 'password2')

# Define un formulario de cambio de usuario personalizado heredando de UserChangeForm
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username')

    # Inicializa el formulario y modifica los campos
    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)  # Llama al método __init__ de la clase base
        self.fields['email'].required = False  # Hace que el campo 'email' no sea obligatorio
        self.fields['username'].required = False  # Hace que el campo 'username' no sea obligatorio

# Define un formulario de autenticación por email heredando de AuthenticationForm
class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='Correo electrónico', max_length=254)

    # Método para limpiar y validar los datos del formulario
    def clean(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if email and password:
            self.user_cache = authenticate(request=self.request, username=email, password=password)
            if self.user_cache is None:  # Si la autenticación falla
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],  # Mensaje de error
                    code='invalid_login',  # Código de error
                    params={'username': self.username_field.verbose_name},  # Parámetros adicionales
                )
            else:
                self.confirm_login_allowed(self.user_cache)  # Confirma si el usuario tiene permitido iniciar sesión
        return self.cleaned_data  # Retorna los datos limpios del formulario

# Define un formulario para el modelo Bonoregalo heredando de ModelForm
class BonoregaloForm(forms.ModelForm):
    class Meta:
        model = Bonoregalo
        fields = ['nombre_receptor', 'apellidos_receptor', 'valor', 'mensaje']  
        widgets = {
            'valor': forms.Select(choices=[(50, '50 €'), (80, '80 €'), (100, '100 €')]),
            'mensaje': forms.Textarea(attrs={'rows': 4}),
        }
