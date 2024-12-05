from django.urls import path
from . import views

urlpatterns = [
    path('medicamentos/', views.lista_medicamentos, name='lista_medicamentos'),
    path('medicamentos/<int:id>/', views.detalle_medicamento, name='detalle_medicamento'),
    path('medicamentos/nuevo/', views.crear_medicamento, name='crear_medicamento'),
]
