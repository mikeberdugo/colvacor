from django.contrib.auth import get_user_model

User = get_user_model()

def authenticate_custom(request, username, password):
    # Implementa tu lógica de verificación de credenciales aquí
    try:
        user = User.objects.get(username=username)
        if user.check_password(password):  # Verifica la contraseña encriptada
            return user
        else:
            return None
    except User.DoesNotExist:
        return None
