from django.db import models

# Create your models here.

import uuid

class Phone(models.Model):
    phone_id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    make=models.CharField(max_length=50)
    model=models.CharField(max_length=50)
    serial_number=models.CharField(max_length=10)
    description=models.TextField()
    purchase_date=models.DateField()
    
    