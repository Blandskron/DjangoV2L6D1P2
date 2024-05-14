from django.urls import path
from . import views

urlpatterns = [
    path('', views.lecciones_list, name='lecciones_list'),
    path('crear/', views.crear_lecciones, name='crear_lecciones'),
    path('<int:id>/', views.detalle_lecciones, name='detalle_lecciones'),
    path('<int:id>/editarleccion/', views.editar_lecciones, name='editar_lecciones'),
    path('<int:id>/eliminarleccion/', views.eliminar_lecciones, name='eliminar_lecciones'),
]
