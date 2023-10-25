from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_teacher = models.BooleanField("is teacher", default=False)
    is_student = models.BooleanField("is student", default=False)
    is_employee = models.BooleanField("is employee", default=False)
    

    