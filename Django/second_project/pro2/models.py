from django.db import models

class UserInfo(models.Model):
    first_name = models.CharField(max_length=264, unique=False)
    last_name = models.CharField(max_length=264, unique=False)
    email = models.CharField(max_length=264, unique=True)
