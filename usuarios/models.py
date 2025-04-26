from django.db import models
from django.contrib.auth.models import User

class InfoExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sports = models.CharField(max_length=40, null=True, blank=True)
    hobbies = models.CharField(max_length=40, null=True, blank=True)
    avatar = models.ImageField(upload_to="avatares", null=True, blank=True)