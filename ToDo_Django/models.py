from django.db import models
from django.contrib.auth.models import User     #(User table used for auth provided by Django)

class todoo(models.Model):
    srno = models.AutoField(primary_key = True, auto_created = True)
    task = models.CharField(max_length=25)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)