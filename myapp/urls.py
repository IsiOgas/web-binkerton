from django.urls import path
from . import views

urlpatterns = [
    path('reportes/', views.reportes, name='reportes'),
    path('', views.home, name='home'),
    path('mapa/', views.mapa, name='mapa'),
    path('infografia/', views.infografia, name='infografia'),
]