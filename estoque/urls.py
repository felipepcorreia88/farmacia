from django.urls import path
from django.views.generic import TemplateView

app_name = 'estoque'

# Placeholder: Essa view genérica será substituída quando você implementar as views reais
placeholder_view = TemplateView.as_view(template_name='admin/base.html')

urlpatterns = [
    # URLs para produtos
    path('produtos/', placeholder_view, name='produto_list'),
    path('produtos/<int:pk>/', placeholder_view, name='produto_detail'),
    path('produtos/novo/', placeholder_view, name='produto_create'),
    path('produtos/<int:pk>/editar/', placeholder_view, name='produto_update'),
    path('produtos/<int:pk>/excluir/', placeholder_view, name='produto_delete'),
    
    # URLs para categorias
    path('categorias/', placeholder_view, name='categoria_list'),
    path('categorias/<int:pk>/', placeholder_view, name='categoria_detail'),
    path('categorias/nova/', placeholder_view, name='categoria_create'),
    path('categorias/<int:pk>/editar/', placeholder_view, name='categoria_update'),
    path('categorias/<int:pk>/excluir/', placeholder_view, name='categoria_delete'),
    
    # URLs para fornecedores
    path('fornecedores/', placeholder_view, name='fornecedor_list'),
    path('fornecedores/<int:pk>/', placeholder_view, name='fornecedor_detail'),
    path('fornecedores/novo/', placeholder_view, name='fornecedor_create'),
    path('fornecedores/<int:pk>/editar/', placeholder_view, name='fornecedor_update'),
    path('fornecedores/<int:pk>/excluir/', placeholder_view, name='fornecedor_delete'),
]