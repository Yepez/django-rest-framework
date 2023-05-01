from django.db import models
from django.utils import timezone

class Employee(models.Model):
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    identificacion = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    edad = models.IntegerField()
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    correo_electronico = models.EmailField()
    fecha_contratacion = models.DateField()
    salario = models.DecimalField(max_digits=8, decimal_places=2)
    cargo = models.CharField(max_length=50)
    supervisor = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno} {self.apellido_materno}"