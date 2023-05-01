from django.db import models
from django.utils import timezone
from product.models import Product

class Inventory(models.Model):
    producto = models.OneToOneField(Product, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0)
    fecha_entrada = models.DateField(default=timezone.now)
    fecha_caducidad = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.producto} - {self.cantidad}'

    def add_quantity(self, cantidad):
        self.cantidad += cantidad
        self.save()

    def remove_quantity(self, cantidad):
        if self.cantidad >= cantidad:
            self.cantidad -= cantidad
            self.save()
        else:
            raise ValueError("Cantidad insuficiente en el inventario")