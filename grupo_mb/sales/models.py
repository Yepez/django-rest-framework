from django.db import models
from django.utils import timezone
from product.models import Product
from employee.models import Employee


class Sale(models.Model):
    fecha_venta = models.DateField(default=timezone.now)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    empleado = models.ForeignKey(Employee, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Product, through='SaleDetail')

    def __str__(self):
        return f'{self.fecha_venta} - {self.empleado} - {self.total}'


class SaleDetail(models.Model):
    venta = models.ForeignKey(Sale, on_delete=models.CASCADE)
    producto = models.ForeignKey(Product, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.venta} - {self.producto} - {self.cantidad}'

