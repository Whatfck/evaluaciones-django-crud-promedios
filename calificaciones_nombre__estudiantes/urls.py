from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'calificaciones'

urlpatterns = [
    # Auth
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='calificaciones:login'), name='logout'),
    path('registro/', views.registro, name='registro'),

    # CRUD
    path('crear/', views.crear_calificacion, name='crear_calificacion'),
    path('', views.listar_calificaciones, name='listar_calificaciones'),
    path('editar/<int:pk>/', views.editar_calificacion, name='editar_calificacion'),
    path('eliminar/<int:pk>/', views.eliminar_calificacion, name='eliminar_calificacion'),
    path('promedio-general/', views.promedio_general, name='promedio_general'),
]
