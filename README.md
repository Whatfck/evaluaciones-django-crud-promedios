# evaluaciones-django-crud-promedios

# **Laboratorio final**

## **Desarrollo de un inicio de sesión y CRUD con Función de Cálculo en Django**

**Contextualización,**

El presente parcial tiene como propósito evaluar las competencias técnicas en el desarrollo de aplicaciones web con el framework **Django**, utilizando la metodología de construcción de un CRUD **(Create, Read, Update, Delete)**. Además, se busca evidenciar la capacidad de aplicar operaciones lógicas o matemáticas dentro del flujo de la aplicación, específicamente el cálculo del **promedio de calificaciones** registrado por un conjunto de estudiantes.

**Objetivo General**

Desarrollar una aplicación en Django que permita, registrar usuarios, inicio de sesión, visualizar, actualizar y eliminar calificaciones de estudiantes, incorporando una función que calcule el **promedio general de notas** o el **promedio individual de cada estudiante**, según los datos almacenados.

**Requerimientos del Proyecto**

**1. Creación del proyecto**
- Crear un proyecto denominado **evaluaciones__nombre__estudiantes** utilizando la versión más reciente de Django.
- Configurar correctamente el entorno virtual y las dependencias requeridas.

**2. Creación de la aplicación**

- Diseñar una aplicación dentro del proyecto con el nombre **calificaciones_nombre__estudiantes**.
- Registrar la aplicación en el archivo settings.py dentro de la lista INSTALLED_APPS.

**3. Definición del modelo**

- Crear un modelo denominado **Calificacion**, que contenga los siguientes campos:
    **- nombre_estudiante:** campo de texto (máximo 150 caracteres).
    **- identificacion:** campo de texto (máximo 15 caracteres).
    **- asignatura:** campo de texto (máximo 100 caracteres).
    **- nota1:** campo de tipo decimal (máximo 5 dígitos, 2 decimales).
    **- nota2:** campo de tipo decimal (máximo 5 dígitos, 2 decimales).
    **- nota3:** campo de tipo decimal (máximo 5 dígitos, 2 decimales).
    **- promedio:** campo calculado, no editable, que almacene el promedio de las tres notas.
- Se solicita incluir una **función personalizada** dentro del modelo para calcular automáticamente el promedio antes de guardar los datos:

```python
def calcular_promedio(self):
return round((self.nota1 + self.nota2 + self.nota3) / 3, 2)
def save(self, *args, **kwargs):
self.promedio = self.calcular_promedio()
super().save(*args, **kwargs)
```

**4. Creación del formulario**

- Definir un formulario en el archivo forms.py basado en el modelo anterior, utilizando la clase ModelForm.
- Excluir el campo promedio del formulario, ya que debe calcularse automáticamente.

**5. Implementación de las vistas (CRUD)**
- Implementar las vistas correspondientes para:

    - **Registrar** una nueva calificación.
    - **Listar** todas las calificaciones registradas.
    - **Editar** una calificación existente.
    - **Eliminar** un registro.

- Adicionalmente, crear una vista que muestre el **promedio general de todos los estudiantes** registrados en la base de datos, calculado mediante una función agregada de Django (Avg).

```python
from django.db.models import Avg
promedio_general =
Calificacion.objects.all().aggregate(Avg('promedio'))['promedio__avg']
```

**6. Configuración de rutas**
- Definir en el archivo urls.py las rutas para cada operación del CRUD.
- Añadir una ruta adicional denominada **promedio-general**, donde se visualizará el
promedio total de los registros.
**7. Creación de las plantillas**
- Elaborar las siguientes plantillas en el directorio templates/calificaciones/:
    - crear.html: formulario para registrar calificaciones.
    -  listar.html: tabla con los registros existentes y el promedio general en la parte inferior.
    - editar.html: formulario para actualizar calificaciones.
    - eliminar.html: página de confirmación para eliminar registros.

**8. Validación y observación del funcionamiento**
- Ejecutar el servidor con el comando python manage.py runserver.
- Verificar la correcta operación de las funciones CRUD y la actualización automática
del campo promedio.
- Validar que el promedio general se calcule y muestre dinámicamente en la vista
correspondiente

|**Criterios de Evaluación**|**Descripción**|**Puntaje**|
|---------------------------|---------------|-----------|
|**Estructura del proyecto**|Correcta creación y configuración del proyecto y aplicación.|0,5 pts|
|**Modelo y lógica de cálculo**|Implementación del modelo con función para cálculo del promedio.|1,0 pts|
|**Vistas CRUD**|Desarrollo funcional de las operaciones Crear, Leer, Actualizar y Eliminar.|1,0 pts|
|**Promedio general**|Cálculo y visualización del promedio total utilizando funciones agregadas.|1,0 pts|
|**Plantillas y presentación**|Estructura visual clara, uso correcto de formularios, plantillas HTML y diseño.|1,5 pts|
|**Ejecución y pruebas**|Funcionamiento completo y libre de errores del sistema.|1,5 pts|
|**Total**| |5,0 pts|