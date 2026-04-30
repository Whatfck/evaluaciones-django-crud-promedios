from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='calificaciones:listar_calificaciones', permanent=False)),
    path('calificaciones/', include(('calificaciones_nombre__estudiantes.urls', 'calificaciones'), namespace='calificaciones')),
]
