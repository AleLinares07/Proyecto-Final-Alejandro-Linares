from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Zapatillas(models.Model):

    modelo = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    talle = models.IntegerField()

    def __str__(self):
        return f'{self.modelo} - {self.color} talle {self.talle}'
    
class Buzos(models.Model):

    modelo = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    talle = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.modelo} - {self.color} talle {self.talle}'
    
class Pantalones(models.Model):

    modelo = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    talle = models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.modelo} - {self.color} talle {self.talle}'
    
class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', blank=True, null=True)
    

