from django.urls import path
from django.views.generic import TemplateView

app_name = 'pessoa'

# Placeholder: Essa view genérica será substituída quando você implementar as views reais
placeholder_view = TemplateView.as_view(template_name='admin/base.html')

urlpatterns = [
    # URLs para clientes
    path('clientes/', placeholder_view, name='cliente_list'),
    path('clientes/<int:pk>/', placeholder_view, name='cliente_detail'),
    path('clientes/novo/', placeholder_view, name='cliente_create'),
    path('clientes/<int:pk>/editar/', placeholder_view, name='cliente_update'),
    path('clientes/<int:pk>/excluir/', placeholder_view, name='cliente_delete'),
    
    # URLs para funcionários
    path('funcionarios/', placeholder_view, name='funcionario_list'),
    path('funcionarios/<int:pk>/', placeholder_view, name='funcionario_detail'),
    path('funcionarios/novo/', placeholder_view, name='funcionario_create'),
    path('funcionarios/<int:pk>/editar/', placeholder_view, name='funcionario_update'),
    path('funcionarios/<int:pk>/excluir/', placeholder_view, name='funcionario_delete'),
    
    # URLs para cargos
    path('cargos/', placeholder_view, name='cargo_list'),
    path('cargos/<int:pk>/', placeholder_view, name='cargo_detail'),
    path('cargos/novo/', placeholder_view, name='cargo_create'),
    path('cargos/<int:pk>/editar/', placeholder_view, name='cargo_update'),
    path('cargos/<int:pk>/excluir/', placeholder_view, name='cargo_delete'),
]