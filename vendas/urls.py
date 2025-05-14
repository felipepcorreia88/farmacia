from django.urls import path
from django.views.generic import TemplateView

app_name = 'vendas'

# Placeholder: Essa view genérica será substituída quando você implementar as views reais
placeholder_view = TemplateView.as_view(template_name='admin/base.html')

urlpatterns = [
    # URLs para vendas
    path('vendas/', placeholder_view, name='venda_list'),
    path('vendas/<int:pk>/', placeholder_view, name='venda_detail'),
    path('vendas/nova/', placeholder_view, name='venda_create'),
    path('vendas/<int:pk>/editar/', placeholder_view, name='venda_update'),
    path('vendas/<int:pk>/excluir/', placeholder_view, name='venda_delete'),
    
    # URLs para itens de venda
    path('itens/', placeholder_view, name='itemvenda_list'),
    path('itens/<int:pk>/', placeholder_view, name='itemvenda_detail'),
    path('itens/novo/', placeholder_view, name='itemvenda_create'),
    path('itens/<int:pk>/editar/', placeholder_view, name='itemvenda_update'),
    path('itens/<int:pk>/excluir/', placeholder_view, name='itemvenda_delete'),
]