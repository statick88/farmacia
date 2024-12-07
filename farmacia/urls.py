from django.urls import path
from . import views
from .views import MedicamentoList, MedicamentoDetail

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API de Medicamentos",
        default_version='v1',
        description="Documentación interactiva de la API",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('', views.lista_medicamentos, name='lista_medicamentos'),
    path('medicamentos/', views.lista_medicamentos, name='lista_medicamentos'),
    path('medicamentos/<int:id>/', views.detalle_medicamento,
         name='detalle_medicamento'),
    path('medicamentos/nuevo/', views.crear_medicamento, name='crear_medicamento'),
    path('medicamentos/editar/<int:id>/',
         views.editar_medicamento, name='editar_medicamento'),
    path('medicamentos/eliminar/<int:id>/',
         views.eliminar_medicamento, name='eliminar_medicamento'),
    path('api/medicamentos/', MedicamentoList.as_view(), name='medicamento-list'),
    path('api/medicamentos/<int:id>/',
         MedicamentoDetail.as_view(), name='medicamento-detail'),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),


]
