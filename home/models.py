from django.db import models
import uuid

class Devices(models.Model):
    
    id = models.UUIDField(default=uuid.uuid4,primary_key=True)
    name = models.CharField(max_length=20,blank=True,null=True)