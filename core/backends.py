from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

# Este método intenta autenticar a un usuario utilizando su email en lugar del nombre de usuario
class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user_model = get_user_model()    # Obtiene el modelo de usuario configurado en el proyecto de Django
        try:
            user = user_model.objects.get(email=username)
        except user_model.DoesNotExist:
            return None
        if user.check_password(password):
            return user
        return None