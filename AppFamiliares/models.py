from django.db import models

# Create your models here.
class Familiar(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=30)
    edad=models.IntegerField(null=True)
    direccion=models.CharField(max_length=40)
    email=models.EmailField()
    tel=models.IntegerField()
    relacion=models.CharField(max_length=20)
    cumpleaños=models.DateField()
