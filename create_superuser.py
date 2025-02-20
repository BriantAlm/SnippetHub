import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tu_proyecto.settings")  # Cambia 'tu_proyecto' por el nombre de tu proyecto
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

def create_superuser():
    username = "admin"
    email = "admin@example.com"
    password = "@dmin_snippets"

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print("Superusuario creado.")
    else:
        print("El superusuario ya existe.")

if __name__ == "__main__":
    create_superuser()
