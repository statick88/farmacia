from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_medicamentos, name='lista_medicamentos'),
    path('medicamentos/', views.lista_medicamentos, name='lista_medicamentos'),
    path('medicamentos/<int:id>/', views.detalle_medicamento, name='detalle_medicamento'),
    path('medicamentos/nuevo/', views.crear_medicamento, name='crear_medicamento'),
    path('medicamentos/editar/<int:id>/', views.editar_medicamento, name='editar_medicamento'),
    path('medicamentos/eliminar/<int:id>/', views.eliminar_medicamento, name='eliminar_medicamento'),
]
