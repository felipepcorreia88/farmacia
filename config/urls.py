from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configuração do Swagger/OpenAPI
schema_view = get_schema_view(
    openapi.Info(
        title="Farmácia API",
        default_version='v1',
        description="API para sistema de gerenciamento de farmácia",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contato@farmacia.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Web views para os apps (interfaces web)
    path('pessoa/', include('pessoa.urls')),
    path('estoque/', include('estoque.urls')),
    path('vendas/', include('vendas.urls')),
    
    # API endpoints por app
    path('api/pessoa/', include('pessoa.api.urls')),
    path('api/estoque/', include('estoque.api.urls')),
    path('api/vendas/', include('vendas.api.urls')),
    
    # API documentation with Swagger
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    # Redirect root to Swagger UI
    path('', lambda request: redirect('schema-swagger-ui')),
]