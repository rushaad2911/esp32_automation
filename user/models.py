from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):
    
    id = models.UUIDField(default=uuid.uuid4,primary_key=True)
    devices = models.CharField(max_length=30,null=True,blank=True)
