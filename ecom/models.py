from email.mime import image
from django.db import models

class mobile_details(models.Model):
    model=models.TextField(max_length=20)
    brand=models.TextField(max_length=20)
    rate=models.IntegerField()
    image=models.ImageField()
   
    class Meta:
        db_table='mobiledetails'
