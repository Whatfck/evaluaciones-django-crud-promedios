"""Plantilla de `views.py` con stubs para las operaciones CRUD.

Los desarrolladores deben implementar las vistas reales en sus respectivas ramas.
"""

from django.shortcuts import render

# TODO: importar modelo y formularios y definir las vistas:
# - crear_calificacion(request)
# - listar_calificaciones(request)
# - editar_calificacion(request, pk)
# - eliminar_calificacion(request, pk)
# - promedio_general(request)

def placeholder(request):
    return render(request, 'calificaciones/placeholder.html')
