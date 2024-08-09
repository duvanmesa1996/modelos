from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.Email.Field()
    telefono = models.CharField(max_length=15)

    def _str_(self):
        return str(self.nombre)

class producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_length=10, decimal_places=2)
    stock = models.IntegerField()

    def _str_(self):
        return str(self.nombre)
        
        