from django.contrib.auth import get_user_model
from .models import Message

class MyAuthenticationBackend:

    def authenticate(self, *args, **kwargs):
        pass


    def get_user(self, user_id):
        try:
            return get_user_model().objects.get(pk=user_id)
        except get_user_model().DoesNotExist:
            return None

