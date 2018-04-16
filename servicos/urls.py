from django.urls import path

from .views import ServicoListView, ServicoDetailView, ServicoCreateView
from .views import PrestadorListView, PrestadorDetailView, gerarArquivo
urlpatterns = [
    path('servico-list/', ServicoListView.as_view(), name='servico-list'),
    path('servico-detail/<int:pk>/', ServicoDetailView.as_view(), name='servico-detail'),
    path('servico-create/', ServicoCreateView.as_view(), name='servico-create'),
    path('prestador-list/', PrestadorListView.as_view(), name='prestador-list'),
    path('prestador-detail/<int:pk>/', PrestadorDetailView.as_view(), name='prestador-detail'),
    path('gerar-arquivo/', gerarArquivo, name="gerar-arquivo"),
]