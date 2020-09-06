from .models import UserKL
import logging
from django.contrib.auth.backends import ModelBackend
import pdb
class UserKLAuthBackend(ModelBackend):
    def authenticate(self,request, email, password):
        try:
            user = UserKL.objects.get(email=email)
            if user.check_password(password):
                return user
            else:
                return None
        except UserKL.DoesNotExist:
            logging.getLogger("error_logger").error("user with login %s does not exists " % email)
            return None
        except Exception as e:
            logging.getLogger("error_logger").error(repr(e))
            return None

    def get_user(self, user_id):
        try:
            return UserKL.objects.get(pk=user_id)
        except UserKL.DoesNotExist:
            return None
