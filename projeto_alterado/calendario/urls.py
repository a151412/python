
from django.urls import path
from .views import home, products, register, exit, calendario, adicionar, create, create_squad, list_squads, edit_squad
from .views import delete_squad, listar_atividades_area, add_freezing_period, edit_freezing_period, list_freezing_periods, delete_freezing_period
from .views import delete, update, edit_atividade, detalhes_atividade, listar_atividades, gerar_pdf, gerar_excel

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SquadViewSet, AtividadesViewSet, FreezingPeriodViewSet

router = DefaultRouter()
router.register(r'squads', SquadViewSet)
router.register(r'atividades', AtividadesViewSet)
router.register(r'freezing-periods', FreezingPeriodViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('gerar-pdf/', gerar_pdf, name='gerar_pdf'),
    path('gerar-excel/', gerar_excel, name='gerar_excel'),
    path('api/', include(router.urls)),
    path('adicionar/', adicionar, name='adicionar'),
    path('listar_atividades/', listar_atividades, name='listar_atividades'),
    path('products/', products, name='products'),
    path('register/', register, name='register'),
    path('logout/', exit, name='exit'),
    path('calendario/', calendario, name='calendario'),
    path('create/', create, name='create'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('create-squad/', create_squad, name='create_squad'),
    path('list_squads/', list_squads, name='list_squads'),
    path('edit-squad/<int:id>/', edit_squad, name='edit_squad'),
    path('delete-squad/<int:id>/', delete_squad, name='delete_squad'),
    path('calendario-area/<int:area_id>/<int:mes>/<int:ano>/', listar_atividades_area, name='listar_atividades_area'),
    path('add_freezing_period/', add_freezing_period, name='add_freezing_period'),
    path('edit_freezing_period/<int:pk>/', edit_freezing_period, name='edit_freezing_period'),
    path('list_freezing_periods/', list_freezing_periods, name='list_freezing_periods'),
    path('delete_freezing_period/<int:pk>/', delete_freezing_period, name='delete_freezing_period'),
    path('detalhes_atividade/<int:pk>/', detalhes_atividade, name='detalhes_atividade'),
    path('edit_atividade/<int:pk>/', edit_atividade, name='edit_atividade'),
]