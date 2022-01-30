from django.contrib.auth.backends import ModelBackend
from .models import User
from django.contrib import admin
class EmailBackend(ModelBackend):
    def authenticate(self, request,email=None,password=None,user_type_obj=None, **kwargs):
        if not email and password:
            return None
        else:
            try:
                user_obj = User.objects.get(user_type=user_type_obj,email__iexact=email)
            except User.DoesNotExist:
                return None
            if user_obj.check_password(password) and super().user_can_authenticate(user_obj) :
                return user_obj
        return None