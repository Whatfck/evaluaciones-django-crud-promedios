from decimal import Decimal

from django.db import migrations


def crear_datos_iniciales(apps, schema_editor):
    Calificacion = apps.get_model('calificaciones_nombre__estudiantes', 'Calificacion')

    def calcular_promedio(nota1, nota2, nota3):
        return round((nota1 + nota2 + nota3) / Decimal('3'), 2)

    datos = [
        {
            'nombre_estudiante': 'Ana María Pérez',
            'identificacion': '1001001',
            'asignatura': 'Matemáticas',
            'nota1': Decimal('4.50'),
            'nota2': Decimal('4.20'),
            'nota3': Decimal('4.80'),
        },
        {
            'nombre_estudiante': 'Luis Fernando Gómez',
            'identificacion': '1001002',
            'asignatura': 'Lengua Castellana',
            'nota1': Decimal('3.80'),
            'nota2': Decimal('4.10'),
            'nota3': Decimal('3.90'),
        },
        {
            'nombre_estudiante': 'Sofía Ramírez',
            'identificacion': '1001003',
            'asignatura': 'Ciencias Naturales',
            'nota1': Decimal('4.90'),
            'nota2': Decimal('4.70'),
            'nota3': Decimal('4.60'),
        },
    ]

    for dato in datos:
        Calificacion.objects.get_or_create(
            nombre_estudiante=dato['nombre_estudiante'],
            identificacion=dato['identificacion'],
            asignatura=dato['asignatura'],
            nota1=dato['nota1'],
            nota2=dato['nota2'],
            nota3=dato['nota3'],
            defaults={'promedio': calcular_promedio(dato['nota1'], dato['nota2'], dato['nota3'])},
        )


class Migration(migrations.Migration):
    dependencies = [
        ('calificaciones_nombre__estudiantes', '0002_alter_calificacion_options'),
    ]

    operations = [
        migrations.RunPython(crear_datos_iniciales, migrations.RunPython.noop),
    ]