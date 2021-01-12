from django.contrib.auth.models import UserManager as AbstractUserManager
from django.db import models


class CustomUserModelManager(AbstractUserManager):
    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except self.model.DoesNotExist:
            return None