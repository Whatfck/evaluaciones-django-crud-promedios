from decimal import Decimal

from django.db import models


class Calificacion(models.Model):
    nombre_estudiante = models.CharField(max_length=150)
    identificacion = models.CharField(max_length=15)
    asignatura = models.CharField(max_length=100)
    nota1 = models.DecimalField(max_digits=5, decimal_places=2)
    nota2 = models.DecimalField(max_digits=5, decimal_places=2)
    nota3 = models.DecimalField(max_digits=5, decimal_places=2)
    promedio = models.DecimalField(max_digits=5, decimal_places=2, editable=False, default=Decimal('0.00'))

    def calcular_promedio(self):
        nota1 = Decimal(self.nota1)
        nota2 = Decimal(self.nota2)
        nota3 = Decimal(self.nota3)
        total = nota1 + nota2 + nota3
        return round(total / Decimal('3'), 2)

    def save(self, *args, **kwargs):
        self.promedio = self.calcular_promedio()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre_estudiante} - {self.asignatura}"
