from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    has_verified_email = models.BooleanField(default=False)