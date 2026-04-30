from django.urls import path, include

urlpatterns = [
    path('calificaciones/', include('calificaciones_nombre__estudiantes.urls')),
]
