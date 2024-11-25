from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Custom User to replace Django's default one."""
