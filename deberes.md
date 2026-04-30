# Deberes por desarrollador (según README)

- **Dev1:** Proyecto, app, modelo y formulario
  - Crear el proyecto Django `evaluaciones__nombre__estudiantes` y configurar el entorno virtual y dependencias.
  - Crear la aplicación `calificaciones_nombre__estudiantes` y registrarla en `settings.py` dentro de `INSTALLED_APPS`.
  - Implementar el modelo `Calificacion` con los campos: `nombre_estudiante`, `identificacion`, `asignatura`, `nota1`, `nota2`, `nota3` y `promedio` (campo no editable).
  - Añadir la función `calcular_promedio` y sobreescribir `save()` para calcular y asignar `promedio` antes de guardar (como indica el README).
  - Definir el `ModelForm` en `forms.py` excluyendo el campo `promedio`.

- **Dev2:** Vistas CRUD y promedio general
  - Implementar las vistas para Registrar, Listar, Editar y Eliminar calificaciones (CRUD).
  - Crear la vista que calcule y muestre el promedio general usando agregaciones de Django (`Avg`) según el ejemplo del README.

- **Dev3:** Rutas y plantillas
  - Definir las rutas en `urls.py` para las operaciones CRUD y la ruta `promedio-general`.
  - Crear las plantillas en `templates/calificaciones/`:
    - `crear.html` (formulario de registro),
    - `listar.html` (tabla con registros y mostrar el promedio general en la parte inferior),
    - `editar.html` (formulario de actualización),
    - `eliminar.html` (confirmación de eliminación).
  - Asegurar que las plantillas presenten los datos según se solicita en el README (estructura clara y uso correcto de formularios).

- **Dev4:** Migraciones, ejecución y validación
  - Ejecutar migraciones y gestionar la integración con la base de datos (crear y aplicar migraciones necesarias).
  - Ejecutar el servidor (`python manage.py runserver`) y verificar la correcta operación de las funciones CRUD y la actualización automática del campo `promedio`.
  - Validar que el promedio general se calcule y muestre dinámicamente en la vista correspondiente, y ayudar a corregir errores detectados durante la validación.

