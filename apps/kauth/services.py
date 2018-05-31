from .models import KUser


def create_user(username: str, password: str, email: str = None, **extra) -> KUser:
    return KUser.objects.create_user(username, email, password, **extra)
