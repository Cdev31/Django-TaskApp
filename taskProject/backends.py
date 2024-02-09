from typing import Any
from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.http import HttpRequest


class EmailAuthBackend( ModelBackend ):

    def authenticate(self, request: HttpRequest, username: str | None = ..., password: str | None = ..., **kwargs: Any) -> AbstractBaseUser | None:
        try:
            user = User.objects.get( email=username )
            
            if user.password == password:
                return user
        except User.DoesNotExist:   
            try: 
                user = User.objects.get( username=username )
                if user.password == password:
                    return user
            except User.DoesNotExist:
                return None 


    def get_user( self, user_id ):
        try:
            return User.objects.get( pk=user_id )
        except User.DoesNotExist:
            return None            