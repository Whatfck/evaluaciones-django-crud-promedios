from decimal import Decimal

from django.db import migrations


def recalcular_promedios(apps, schema_editor):
    Calificacion = apps.get_model('calificaciones_nombre__estudiantes', 'Calificacion')

    for calificacion in Calificacion.objects.all():
        calificacion.promedio = round(
            (Decimal(calificacion.nota1) + Decimal(calificacion.nota2) + Decimal(calificacion.nota3)) / Decimal('3'),
            2,
        )
        calificacion.save(update_fields=['promedio'])


class Migration(migrations.Migration):
    dependencies = [
        ('calificaciones_nombre__estudiantes', '0003_datos_iniciales'),
    ]

    operations = [
        migrations.RunPython(recalcular_promedios, migrations.RunPython.noop),
    ]