from .models import UserProfile


def create_user_profile(user, first_name=None, phone=None):
    UserProfile.objects.create(user=user, first_name=first_name, phone=phone)
