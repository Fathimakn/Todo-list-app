from django.db import models
from django.contrib.auth.models import User
class Task(models.Model):
    title=models.CharField(max_length=255)
    completed=models.BooleanField(default=False)#by default it should be false
    created_on=models.DateField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)



# Create your models here.
