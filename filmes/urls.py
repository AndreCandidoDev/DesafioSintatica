from django.urls import path
from .views import avaliacoes_list, avaliacao_create

urlpatterns = [
    path('avaliacoes/', avaliacoes_list, name='avaliacoes'),
    path('nova_avaliacao/', avaliacao_create, name='avaliacao_create')
]