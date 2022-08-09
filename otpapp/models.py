from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class customers(models.Model):
    id = models.AutoField(primary_key=True)
    otp = models.IntegerField()
    isverify = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
