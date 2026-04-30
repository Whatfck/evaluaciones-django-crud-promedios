"""Plantilla de `models.py` para la app `calificaciones_nombre__estudiantes`.

Esta plantilla NO implementa lógica, solo muestra la estructura sugerida.
Sustituir y completar al implementar el modelo real.
"""

from django.db import models

class Calificacion(models.Model):
    """Modelo `Calificacion` — campos sugeridos:

    - nombre_estudiante: CharField(max_length=150)
    - identificacion: CharField(max_length=15)
    - asignatura: CharField(max_length=100)
    - nota1, nota2, nota3: DecimalField(max_digits=5, decimal_places=2)
    - promedio: DecimalField(max_digits=5, decimal_places=2, editable=False)

    Implementar `calcular_promedio` y `save()` en la versión final.
    """

    # TODO: definir los campos reales aquí
    pass
