from django.db import models
from django.contrib.auth.models import User


class Info(models.Model):
    user = models.ForeignKey(User, related_name='info', unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField('Date of birth')
    bio = models.CharField(max_length=255)
    contacts = models.CharField(max_length=255)
